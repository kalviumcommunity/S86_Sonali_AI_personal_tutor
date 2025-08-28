import streamlit as st
from src.groq_client import get_ai_response, build_zero_shot_prompt, build_one_shot_prompt, build_multi_shot_prompt

# Streamlit page configuration
st.set_page_config(
    page_title="AI Personal Tutor",
    page_icon=":books:",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("Project Info")
    st.markdown("""
    **AI Personal Tutor**  
    This project is an AI-powered tutor that can assist with any topic or question.
    """)

    st.markdown("---")
    st.subheader("Sample Usage / Test Inputs")
    st.markdown("""
    **Try these example questions:**  
    - What is the React Hooks? 
    - Explain Python Data Types?
    - How does blockchain work?  
    """)

    st.markdown("---")
    st.subheader("Select Prompt Type")
    prompt_type = st.radio(
        "Prompt Type:", ["Zero-Shot", "One-Shot", "Multi-Shot"])

# Main Page
st.title("AI Personal Tutor")
st.write("Ask a question or request help on any topic, and get step-by-step explanations!")

# User input
question = st.text_input("Enter your question or topic:")
submit = st.button("Get Answer")

if submit and question:
    # Build prompt dynamically based on sidebar selection
    if prompt_type == "Zero-Shot":
        prompt = build_zero_shot_prompt("General", question)
    elif prompt_type == "One-Shot":
        prompt = build_one_shot_prompt("General", question)
    else:
        prompt = build_multi_shot_prompt("General", question)

    # Get AI response
    answer = get_ai_response(prompt)

    # Display result
    st.markdown("**Answer:**")
    st.write(answer)
