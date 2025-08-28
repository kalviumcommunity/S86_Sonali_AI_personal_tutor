from groq import Groq
from src.config import GROQ_API_KEY

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)


def build_zero_shot_prompt(topic, question):
    """
    Zero-Shot: AI answers directly without examples.
    """
    return f"""
You are an AI tutor. Answer the following {topic} question directly.
Explain your answer step by step.

Question: {question}
"""


def build_one_shot_prompt(topic, question):
    """
    One-Shot: AI is given a single example to guide its response.
    """
    return f"""
You are an AI tutor. Answer the following {topic} question.
Explain your answer step by step.

Example Q&A:
1) Q: What is the boiling point of water? 
   A: 100°C at standard atmospheric pressure.

Question: {question}
"""


def build_multi_shot_prompt(topic, question):
    """
    Multi-Shot: AI is given multiple examples to guide its response.
    """
    return f"""
You are an AI tutor. Answer the following {topic} question.
Explain your answer step by step.

Example Q&A:
1) Q: What is the boiling point of water? 
   A: 100°C at standard atmospheric pressure.
2) Q: Who wrote 'Romeo and Juliet'? 
   A: William Shakespeare.
3) Q: What is the capital of France? 
   A: Paris.

Question: {question}
"""


def get_ai_response(prompt, stream=False):
    """
    Calls the Groq LLM with the provided prompt.
    Supports streaming with the smaller 8B instant model.
    Logs tokens if stream=False.
    """
    if stream:
        # Streaming response
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=True,
            stop=None
        )

        response_text = ""
        for chunk in completion:
            delta = chunk.choices[0].delta
            content = delta.get("content", "")
            print(content, end="", flush=True)
            response_text += content
        print()  # newline after streaming
        return response_text
    else:
        # Standard response
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
        )
        tokens_used = response.usage.total_tokens
        print(f"Tokens used: {tokens_used}")
        return response.choices[0].message.content
