

# **AI Personal Tutor**

---

## **Project Overview**

**AI Personal Tutor** is an interactive educational application that allows users to ask questions in various subjects such as Math, Science, and History. The AI provides **step-by-step explanations**, making learning more intuitive and personalized.

This project is built using **Streamlit** for the UI and **Groq LLM** for AI responses. It demonstrates **8 core GenAI/LLM concepts**, including advanced prompt engineering techniques.

---

## **Key Features**

* **Interactive Q\&A** – Users can ask questions in different subjects and get detailed answers.
* **Dynamic Prompts** – The AI response adapts based on the user-selected subject.
* **Step-by-Step Explanations** – The AI explains its reasoning, supporting learning and understanding.
* **Token Logging** – Logs the number of tokens used for each AI call to monitor usage and efficiency.
* **Example-Based Learning** – Uses zero-shot, one-shot, and multi-shot prompting to guide AI responses.

---

## **GenAI Concepts Covered**

1. **Create Project Readme** – This file explains the project clearly.
2. **System and User Prompt** – Separates AI system role and user input in prompts.
3. **Zero-Shot Prompting** – AI answers questions without examples.
4. **One-Shot Prompting** – Includes a single example Q\&A to guide the AI.
5. **Multi-Shot Prompting** – Includes multiple example Q\&As for higher accuracy.
6. **Dynamic Prompting** – Prompts are updated based on the user-selected subject and question.
7. **Chain of Thought Prompting** – AI explains answers step by step.
8. **Tokens and Tokenization** – Logs the number of tokens used per AI call.

---

## **Tech Stack**

* **Frontend/UI**: Streamlit
* **AI/Backend**: Groq LLM
* **Environment Management**: Python-dotenv
* **Data Validation**: Pydantic (for user inputs)
* **Programming Language**: Python

---

## **Folder Structure**

```
ai_personal_tutor_tokens/
├── assets/
│   └── logo.png
├── app.py
├── groq_client.py
├── requirements.txt
├── config.py
└── README.md
```

---

## **Setup Instructions**

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/ai_personal_tutor_tokens.git
cd ai_personal_tutor_tokens
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Configure Environment Variables**

Create a `.env` file in the root folder and add your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

4. **Run the Application**

```bash
streamlit run app.py
```

---

## **How It Works**

1. Open the app in the browser.
2. Enter your question in the text input field.
3. Select a subject from the dropdown menu.
4. Click **Get Answer**.
5. The AI generates a step-by-step explanation and displays it in the UI.
6. The number of tokens used for each response is logged in the terminal.

---

## **Example Prompt Used in App**

```python
prompt = f"""
You are an AI tutor. Answer the following {subject} question.
Explain your answer step by step.

Question: {question}

Example Q&A:
1) What is 2+2? -> 4
2) Who discovered gravity? -> Isaac Newton
"""
```

This prompt demonstrates **dynamic prompting**, **chain of thought**, **one-shot**, and **multi-shot prompting**.

---

## **Future Enhancements**

* Add **voice input** for questions.
* Include **more subjects** and topics.
* Store **previous questions** and answers using embeddings and vector databases.
* Add **quiz mode** for interactive learning.
* Improve UI with **Bro UI or custom Streamlit components**.

---

## **Conclusion**

This AI Personal Tutor is a **lightweight, practical, and educational application** that demonstrates **8 key GenAI concepts**. It can be further extended into a complete learning assistant with gamification, analytics, and multi-modal inputs.
