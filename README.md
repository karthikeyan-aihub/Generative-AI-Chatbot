# 🤖 Generative AI Chatbot

A memory-enabled Generative AI chatbot built using **Gradio**, **LangChain**, and **Groq (Llama 3.3)**.

The application provides interactive, context-aware conversations through a clean web interface while maintaining chat history using LangChain memory.

---

## ✨ Features

- 💬 Interactive chat interface using Gradio
- 🧠 Conversational memory with LangChain
- ⚡ Powered by Groq (`llama-3.3-70b-versatile`)
- 🔐 Secure API key handling using environment variables
- 🌍 Deployable on Hugging Face Spaces
- 🚀 Fast inference using Groq Cloud

---

## 🛠️ Technologies Used

- Python
- Gradio
- LangChain
- Groq API
- Llama 3.3 70B Versatile
- GitHub
- Hugging Face Spaces

---

## 📁 Project Structure

```
Generative-AI-Chatbot/
│
├── app.py
├── requirements.txt
├── README.md
└── LICENSE (optional)
```

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Generative-AI-Chatbot.git
cd Generative-AI-Chatbot
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set the Groq API Key

**Windows (PowerShell)**

```powershell
$env:GROQ_API_KEY="gsk_your_api_key"
```

**Windows (CMD)**

```cmd
set GROQ_API_KEY=gsk_your_api_key
```

**Linux / macOS**

```bash
export GROQ_API_KEY="gsk_your_api_key"
```

### 4️⃣ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:7860
```

---

## 🌍 Deployment

This project can be deployed easily on **Hugging Face Spaces**.

1. Create a new **Gradio Space**.
2. Upload the project files.
3. Go to **Settings → Variables and Secrets**.
4. Add a new secret:

| Name | Value |
|------|------|
| `GROQ_API_KEY` | `gsk_your_api_key` |

5. Restart the Space.

---

## 📦 Requirements

```
gradio>=5.0.0
langchain>=0.3.0
langchain-core>=0.3.0
langchain-groq>=0.2.0
```

---

## 📸 Demo

*(Add a screenshot or GIF of your chatbot here.)*

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Karthikeyan S**

- 🎓 B.E. Computer Science Engineering (AI & ML)
- 🏫 Annamalai University
- 💼 AI & Machine Learning Enthusiast
- 🌐 GitHub: https://github.com/karthikeyan-2005
