# -AI-PDF-Chatbot-project
An AI-powered Document Q&amp;A Chatbot built with Python, Streamlit, and Google Gemini API that lets users upload PDF files and ask context-aware questions.
# 🤖 AI Document Q&A Chatbot

An interactive, AI-powered web application that allows users to upload any text-based PDF document and ask questions about its content. Built using **Python**, **Streamlit**, and the **Google Gemini API**.

---

## ✨ Features
- **PDF Text Extraction:** Automatically reads and extracts text from uploaded PDF files using `pypdf`.
- **Context-Aware Answers:** Uses Google's `gemini-2.5-flash` model to provide accurate answers strictly based on the uploaded document.
- **Interactive Chat Interface:** Clean, real-time chat UI with persistent session chat history powered by `Streamlit`.
- **Secure API Handling:** Users can securely input their own Google Gemini API key via the sidebar without hardcoding credentials.

---

## 🛠️ Tech Stack
- **Language:** Python
- **Frontend UI:** Streamlit
- **AI Model:** Google Gemini API (`google-genai`)
- **PDF Processing:** PyPDF (`pypdf`)

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/MHassanaABCD]
```

### 2. Install Required Libraries
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
streamlit run app.py
```

### 4. Use the App
1. Get a free API key from [Google AI Studio](https://google.com).
2. Paste the API key into the app's sidebar.
3. Upload a PDF document and start chatting!

---

## 📂 Project Structure
```text
├── app.py              # Main Streamlit application & Gemini API integration
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```
