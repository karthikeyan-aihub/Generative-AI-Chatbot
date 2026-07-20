# 🌍 Hugging Face Deployment Documentation

## Generative AI Chatbot (Gradio + LangChain + Groq)

---

# 1. Introduction

This document describes the **deployment, access, and embedding** of the **Generative AI Chatbot** hosted on **Hugging Face Spaces**.

The chatbot is built using **Gradio**, **LangChain**, and **Groq Cloud (Llama 3.3)** and is deployed as a publicly accessible web application.

This documentation focuses exclusively on the Hugging Face deployment, including:

* Deployment
* Public access
* GitHub integration
* Embedding methods
* Secure API key management

---

# 2. Hugging Face Space Overview

* **Platform:** Hugging Face Spaces
* **SDK:** Gradio
* **LLM Provider:** Groq Cloud
* **Model:** `llama-3.3-70b-versatile`
* **Framework:** LangChain
* **Deployment Type:** GitHub-integrated Space
* **Visibility:** Public

The application is automatically built and deployed whenever changes are pushed to the connected GitHub repository.

---

# 3. Live Application URL

The chatbot can be accessed using the following public URL:

**https://karthikeyan05ai-generative-ai-chatbot.hf.space**

### Use Cases

* Live demonstrations
* Academic project showcase
* Portfolio presentation
* Instant access without local installation

---

# 4. GitHub Integration with Hugging Face

The Hugging Face Space is connected directly to a GitHub repository.

### Deployment Workflow

```
GitHub Repository
        │
        ▼
Hugging Face Spaces
        │
        ▼
 Automatic Build
        │
        ▼
 Gradio Application
        │
        ▼
     End Users
```

### Benefits

* Automatic deployment after every GitHub push
* Version-controlled source code
* Simplified maintenance and updates
* Continuous integration workflow

---

# 5. Secure API Key Management

The Groq API key is **never stored in the source code**.

Instead, Hugging Face Spaces **Secrets** are used to securely provide the API key during runtime.


### Security Benefits

* API key remains hidden
* Safe for public GitHub repositories
* Prevents accidental credential exposure
* Follows industry best practices

---

# 6. Embedding the Hugging Face Application

Hugging Face provides multiple ways to embed the deployed Gradio application.

---

## 6.1 Direct URL Access

Users can access the chatbot directly through any web browser.

**https://karthikeyan05ai-generative-ai-chatbot.hf.space**

### Recommended For

* Portfolio websites
* GitHub README files
* Academic demonstrations
* Mobile and desktop access

---

## 6.2 Gradio Web Component Embed

The chatbot can be embedded into any HTML webpage using the Gradio Web Component.

### Embed Code

```html
<script
  type="module"
  src="https://gradio.s3-us-west-2.amazonaws.com/6.2.0/gradio.js">
</script>

<gradio-app src="https://karthikeyan05ai-generative-ai-chatbot.hf.space"></gradio-app>
```

### Recommended For

* Personal portfolio websites
* College project pages
* Technical blogs
* Documentation websites

---

# 7. Deployment Architecture

```
                 User
                  │
                  ▼
         Web Browser
                  │
                  ▼
       Hugging Face Spaces
                  │
                  ▼
        Gradio Web Interface
                  │
                  ▼
      LangChain Application
                  │
                  ▼
        Groq Cloud API
                  │
                  ▼
 Llama 3.3 70B Versatile Model
```

---

# 8. Advantages of Hugging Face Spaces

* Free hosting for Gradio applications
* Automatic deployment from GitHub
* Easy public sharing through a unique URL
* Secure environment variable management
* Built-in support for machine learning applications
* No manual server configuration required

---

# 9. Conclusion

The Generative AI Chatbot is successfully deployed on **Hugging Face Spaces** using **Gradio**, **LangChain**, and **Groq Cloud's Llama 3.3 model**.

By integrating GitHub with Hugging Face Spaces and securely managing the `GROQ_API_KEY` using Hugging Face Secrets, the application remains secure, maintainable, and easily accessible for demonstrations, academic presentations, and portfolio purposes.
