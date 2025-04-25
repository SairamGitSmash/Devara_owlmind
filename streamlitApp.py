# import streamlit as st
# from dotenv import dotenv_values
# from owlmind.pipeline import ModelProvider

# # Load environment variables
# config = dotenv_values('.env')
# URL = config['SERVER_URL']
# MODEL = config.get('SERVER_MODEL')
# TYPE = config.get('SERVER_TYPE')
# API_KEY = config.get('SERVER_API_KEY')

# # Initialize the model provider
# provider = ModelProvider(type=TYPE, base_url=URL, api_key=API_KEY, model=MODEL)

# # Set up Streamlit UI
# st.set_page_config(page_title="Devara_Bot – AI Study Companion", layout="centered")
# st.title("🤖 Devara_Bot")
# st.subheader("Your AI Study Companion")

# # Initialize memory
# if 'chat_history' not in st.session_state:
#     st.session_state.chat_history = []

# # Tabs for navigation
# tab1, tab2, tab3 = st.tabs(["Ask AI", "Schedule", "Quiz"])

# # --- TAB 1: Ask AI ---
# with tab1:
#     st.markdown("### 💬 How can I assist you in your studies?")
#     st.markdown("<style>.stTextInput>div>div>input { padding: 12px 16px; font-size: 16px; border-radius: 10px; border: 1px solid #ccc; }</style>", unsafe_allow_html=True)
#     question = st.text_input("", placeholder="Type your question here (e.g., What is IoT?)", key="user_question")
#     col1, col2 = st.columns([1, 1])
#     with col1:
#         if st.button("📤 Ask", key="ask_btn"):
#             if question.strip():
#                 st.session_state.chat_history.append({"role": "user", "content": question})
#                 prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.chat_history])
#                 with st.spinner("Thinking..."):
#                     response = provider.request(prompt)
#                     st.session_state.chat_history.append({"role": "assistant", "content": response})
#                     st.success("Response:")
#                     st.markdown(response)
#             else:
#                 st.warning("Please enter a question.")
#     with col2:
#         if st.button("🔄 Reset Chat", key="reset_btn"):
#             st.session_state.chat_history.clear()
#             st.experimental_rerun()

#     if st.session_state.chat_history:
#         st.markdown("---")
#         st.markdown("#### 🧠 Conversation History")
#         for msg in st.session_state.chat_history:
#             st.write(f"**{msg['role'].capitalize()}**: {msg['content']}")

# # --- TAB 2: Study Schedule ---
# with tab2:
#     st.markdown("### 📅 Personalized Study Schedule")
#     if st.button("📅 Generate Today’s Schedule", key="schedule_btn"):
#         prompt = "Create a Pomodoro-style study schedule for today covering AI, Python, and ML."
#         with st.spinner("Generating schedule..."):
#             response = provider.request(prompt=prompt)
#             st.markdown(response)

# # --- TAB 3: Quiz Generator ---
# with tab3:
#     st.markdown("### 🧠 Quick Quiz")
#     topic = st.selectbox("Choose a topic", ["Python", "Machine Learning", "AI", "Data Structures"], key="quiz_topic")
#     if st.button("🧪 Generate Quiz", key="quiz_btn"):
#         prompt = f"Generate a multiple-choice quiz question on the topic: {topic}"
#         with st.spinner("Generating quiz question..."):
#             response = provider.request(prompt=prompt)
#             st.markdown(response)

# # Footer
# st.markdown("---")
# st.caption("Built with ❤️ by COT6930 Final Project")
# st.markdown("Devara_Bot Team")










# import streamlit as st
# from dotenv import dotenv_values
# from owlmind.pipeline import ModelProvider

# # Load environment variables
# config = dotenv_values('.env')
# URL = config['SERVER_URL']
# MODEL = config.get('SERVER_MODEL')
# TYPE = config.get('SERVER_TYPE')
# API_KEY = config.get('SERVER_API_KEY')

# # Initialize the model provider
# provider = ModelProvider(type=TYPE, base_url=URL, api_key=API_KEY, model=MODEL)

# # Set up Streamlit UI
# st.set_page_config(page_title="Devara_Bot – AI Study Companion", layout="centered")

# # Theme toggle
# dark_mode = st.toggle("🌗 Dark Mode")

# # CSS Styling
# st.markdown(f"""
#     <style>
#         .stChatBubble {{
#             border-radius: 1rem;
#             padding: 1rem;
#             margin: 0.5rem 0;
#             max-width: 100%;
#             line-height: 1.6;
#             word-wrap: break-word;
#         }}
#         .stChatBubble.user {{
#             background-color: {'#2e3a59' if dark_mode else '#e0f7fa'};
#             color: {'white' if dark_mode else 'black'};
#             text-align: right;
#         }}
#         .stChatBubble.assistant {{
#             background-color: {'#1f2937' if dark_mode else '#fff3e0'};
#             color: {'white' if dark_mode else 'black'};
#             text-align: left;
#         }}
#         .stButton>button {{
#             padding: 10px 20px;
#             border-radius: 10px;
#             font-size: 16px;
#         }}
#     </style>
# """, unsafe_allow_html=True)

# st.title("🤖 Devara_Bot")
# st.subheader("Your AI Study Companion")

# # Initialize memory
# if 'chat_history' not in st.session_state:
#     st.session_state.chat_history = []

# # Tabs for navigation
# tab1, tab2, tab3 = st.tabs(["Ask AI", "Schedule", "Quiz"])

# # --- TAB 1: Ask AI ---
# with tab1:
#     st.markdown("### 💬 How can I assist you in your studies?")
#     question = st.text_input("", placeholder="Type your question here (e.g., What is IoT?)", key="user_question")
#     col1, col2 = st.columns([1, 1])

#     with col1:
#         if st.button("📤 Ask", key="ask_btn"):
#             if question.strip():
#                 st.session_state.chat_history.append({"role": "user", "content": question})
#                 prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.chat_history])
#                 with st.spinner("Thinking..."):
#                     response = provider.request(prompt)
#                     st.session_state.chat_history.append({"role": "assistant", "content": response})
#                     st.success("Response:")
#                     st.markdown(f"<div class='stChatBubble assistant'>{response}</div>", unsafe_allow_html=True)
#             else:
#                 st.warning("Please enter a question.")

#     with col2:
#         if st.button("🔄 Reset Chat", key="reset_btn"):
#             st.session_state.chat_history.clear()
#             st.experimental_rerun()

#     if st.session_state.chat_history:
#         st.markdown("---")
#         st.markdown("#### 🧠 Conversation History")
#         for msg in st.session_state.chat_history:
#             bubble_class = "user" if msg["role"] == "user" else "assistant"
#             st.markdown(f"<div class='stChatBubble {bubble_class}'>{msg['content']}</div>", unsafe_allow_html=True)

# # --- TAB 2: Study Schedule ---
# with tab2:
#     st.markdown("### 🗓️ Personalized Study Schedule")
#     if st.button("🗓️ Generate Today’s Schedule", key="schedule_btn"):
#         prompt = "Create a Pomodoro-style study schedule for today covering AI, Python, and ML."
#         with st.spinner("Generating schedule..."):
#             response = provider.request(prompt=prompt)
#             st.markdown(f"<div class='stChatBubble assistant'>{response}</div>", unsafe_allow_html=True)

# # --- TAB 3: Quiz Generator ---
# with tab3:
#     st.markdown("### 🧠 Quick Quiz")
#     topic = st.selectbox("Choose a topic", ["Python", "Machine Learning", "AI", "Data Structures"], key="quiz_topic")
#     if st.button("🧪 Generate Quiz", key="quiz_btn"):
#         prompt = f"Generate a multiple-choice quiz question on the topic: {topic}"
#         with st.spinner("Generating quiz question..."):
#             response = provider.request(prompt=prompt)
#             st.markdown(f"<div class='stChatBubble assistant'>{response}</div>", unsafe_allow_html=True)

# # Footer
# st.markdown("---")
# st.caption("Built with ❤️ by COT6930 Final Project")
# st.markdown("Devara_Bot Team")


















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

# Set up Streamlit UI
st.set_page_config(page_title="Devara_Bot – AI Study Companion", layout="centered")

# Theme toggle
dark_mode = st.toggle("🌗 Dark Mode")

# CSS Styling
st.markdown(f"""
    <style>
        html, body {{ font-family: 'Segoe UI', sans-serif; }}
        .stChatBubble {{
            border-radius: 1rem;
            padding: 1rem;
            margin: 0.5rem 0;
            max-width: 100%;
            line-height: 1.6;
            word-wrap: break-word;
        }}
        .stChatBubble.user {{
            background-color: {'#2e3a59' if dark_mode else '#e0f7fa'};
            color: {'white' if dark_mode else 'black'};
            text-align: right;
        }}
        .stChatBubble.assistant {{
            background-color: {'#1f2937' if dark_mode else '#fff3e0'};
            color: {'white' if dark_mode else 'black'};
            text-align: left;
        }}
        .stButton>button {{
            padding: 10px 20px;
            border-radius: 10px;
            font-size: 16px;
            transition: background-color 0.3s ease;
        }}
        .stTextInput>div>div>input {{
            padding: 12px 16px;
            font-size: 16px;
            border-radius: 10px;
            border: 1px solid #ccc;
        }}
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center;'>
        <h1>🤖 Devara_Bot</h1>
        <h3 style='opacity: 0.8;'>Your AI Study Companion</h3>
    </div>
""", unsafe_allow_html=True)

# Initialize memory
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Tabs for navigation
tab1, tab2, tab3 = st.tabs(["Ask AI", "Schedule", "Quiz"])

# --- TAB 1: Ask AI ---
with tab1:
    st.markdown("### 💬 Ask Anything")
    question = st.text_input("", placeholder="Ask your study-related question here...", key="user_question")
    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("📤 Ask", key="ask_btn"):
            if question.strip():
                st.session_state.chat_history.append({"role": "user", "content": question})
                prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.chat_history])
                with st.spinner("Devara_Bot is thinking..."):
                    response = provider.request(prompt)
                    st.session_state.chat_history.append({"role": "assistant", "content": response})
                    st.success("Response:")
                    st.markdown(f"<div class='stChatBubble assistant'>{response}</div>", unsafe_allow_html=True)
            else:
                st.warning("Please enter a question.")

    with col2:
        if st.button("🔄 Reset Chat", key="reset_btn"):
            st.session_state.chat_history.clear()
            st.experimental_rerun()

    if st.session_state.chat_history:
        st.markdown("---")
        st.markdown("#### 🧠 Chat History")
        for msg in st.session_state.chat_history:
            bubble_class = "user" if msg["role"] == "user" else "assistant"
            st.markdown(f"<div class='stChatBubble {bubble_class}'>{msg['content']}</div>", unsafe_allow_html=True)

# --- TAB 2: Study Schedule ---
with tab2:
    st.markdown("### 📅 Personalized Study Schedule")
    if st.button("🗓️ Generate Today’s Schedule", key="schedule_btn"):
        prompt = "Create a Pomodoro-style study schedule for today covering AI, Python, and ML."
        with st.spinner("Generating your schedule..."):
            response = provider.request(prompt=prompt)
            st.markdown(f"<div class='stChatBubble assistant'>{response}</div>", unsafe_allow_html=True)

# --- TAB 3: Quiz Generator ---
with tab3:
    st.markdown("### 🧠 Quick Quiz Generator")
    topic = st.selectbox("Choose a topic", ["Python", "Machine Learning", "AI", "Data Structures"], key="quiz_topic")
    if st.button("🧪 Generate Quiz", key="quiz_btn"):
        prompt = f"Generate a multiple-choice quiz question on the topic: {topic}"
        with st.spinner("Preparing quiz question..."):
            response = provider.request(prompt=prompt)
            st.markdown(f"<div class='stChatBubble assistant'>{response}</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("Built with ❤️ by COT6930 Final Project")
st.markdown("<div style='text-align: center; font-size: 14px;'>Devara_Bot Team</div>", unsafe_allow_html=True)