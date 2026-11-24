import streamlit as st
from pypdf import PdfReader
from google import genai
from google.genai import types

# Page ki setting
st.set_page_config(page_title="AI PDF Chatbot", page_icon="🤖")
st.title("🤖 AI Document Chatbot")
st.caption("Apni PDF file upload karein aur uske baray mein kuch bhi puchein!")

# Sidebar mein API Key aur File Upload
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Google Gemini API Key daalein:", type="password")
    st.markdown("[Free API Key yahan se lein](https://google.com)")
    
    uploaded_file = st.file_uploader("Apni PDF file upload karein", type=["pdf"])
    
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# PDF se text nikalne ka function
@st.cache_data
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    return text

# Chat history initialize karein
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani chat messages screen par dikhayein
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Agar PDF upload ho gayi hai toh text extract karein
pdf_text = ""
if uploaded_file is not None:
    pdf_text = extract_text_from_pdf(uploaded_file)
    st.sidebar.success("PDF successfully parh li gayi hai!")

# User ka sawal (Chat Input)
if prompt := st.chat_input("Apna sawal yahan likhein..."):
    if not api_key:
        st.error("Meherbani karke pehle sidebar mein apni Gemini API Key daalein.")
        st.stop()
    if not uploaded_file:
        st.warning("Pehle koi PDF file upload karein.")
        st.stop()

    # User ka message screen par dikhayein aur save karein
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI se jawab generate karein
    with st.chat_message("assistant"):
        with st.spinner("Soch raha hoon..."):
            try:
                client = genai.Client(api_key=api_key)
                
                system_instruction = (
                    "Tum ek helpful AI assistant ho. Neeche diye gaye document ke text ki buniyad par "
                    "user ke sawalon ka jawab do. Agar jawab document mein maujood nahi hai, toh saaf keh do "
                    "ke yeh maloomat document mein nahi hai.\n\n"
                    f"Document Text:\n{pdf_text}"
                )

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=0.3,
                    )
                )
                
                answer = response.text
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
                
            except Exception as e:
                st.error(f"Error aa gaya: {e}")
