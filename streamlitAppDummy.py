import streamlit as st
from dotenv import dotenv_values
from owlmind.pipeline import ModelProvider

# Load environment variables
config = dotenv_values('.env')
URL = config['SERVER_URL']
MODEL = config.get('SERVER_MODEL')
TYPE = config.get('SERVER_TYPE')
API_KEY = config.get('SERVER_API_KEY')

# Initialize the model provider
provider = ModelProvider(type=TYPE, base_url=URL, api_key=API_KEY, model=MODEL)

# Streamlit page setup
st.set_page_config(page_title="Devara_Bot – AI with Memory", layout="centered")
st.title("🧠 Devara_Bot with Memory")



# Custom CSS for dark theme styling
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: white;
        }
        .block-container {
            padding-top: 2rem;
        }
        .stButton>button {
            color: white;
            background-color: #4a6fe3;
            border-radius: 8px;
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.image("https://img.icons8.com/emoji/48/robot-emoji.png", width=48)
st.title("Devara_Bot")
st.subheader("AI Study Companion")

# Tabs for features
tab1, tab2, tab3 = st.tabs(["Ask AI", "Schedule", "Quiz"])

# Tab 1: Ask AI
with tab1:
    st.markdown("### 🤖 How can I assist you in your studies?")
    question = st.text_input("Ask anything (e.g., What is IoT?)")
    if st.button("Ask"):
        if question.strip():
            with st.spinner("Generating response..."):
                response = provider.request(prompt=question)
                st.success("Response:")
                st.markdown(response)
        else:
            st.warning("Please enter a question.")

# Tab 2: Study Schedule
with tab2:
    st.markdown("### 🗓️ Personalized Study Schedule")
    if st.button("Generate Today’s Schedule"):
        prompt = "Create a Pomodoro-style study schedule for today covering AI, Python, and ML."
        with st.spinner("Generating schedule..."):
            response = provider.request(prompt=prompt)
            st.info(response)

# Tab 3: Quiz Generator
with tab3:
    st.markdown("### 🧠 Quick Quiz")
    topic = st.selectbox("Choose a topic", ["Python", "Machine Learning", "AI", "Data Structures"])
    if st.button("Generate Quiz"):
        prompt = f"Generate a multiple-choice quiz question on the topic: {topic}"
        with st.spinner("Generating quiz question..."):
            response = provider.request(prompt=prompt)
            st.markdown(response)

# Footer
st.markdown("---")
st.caption("Built with ❤️ for COT6930 by the Devara_Bot Team")
