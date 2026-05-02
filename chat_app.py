"""
ChatGPT-like Chat Application built with Streamlit.

This app simulates a conversational AI interface without using any external
LLM or API. Responses are generated locally by a simple Python function
that picks replies based on keyword matching and random selection.

Run with:
    streamlit run chat_app.py
"""

import random
import streamlit as st

# ── Page configuration ──────────────────────────────────────────────────────

st.set_page_config(
    page_title="ChatGPT-like App",
    page_icon="💬",
    layout="centered",
)

# ── Mock response generator ─────────────────────────────────────────────────


def generate_mock_response(user_message: str) -> str:
    """Return a simulated assistant reply based on the user's message.

    Uses keyword matching to provide contextually relevant responses.
    Falls back to a random generic reply when no keywords match.
    No external LLM or API is used.
    """
    text = user_message.lower().strip()

    # Greeting patterns
    if any(word in text for word in ["hello", "hi", "hey", "greetings", "good morning", "good evening"]):
        return random.choice([
            "Hello! How can I help you today?",
            "Hey there! What's on your mind?",
            "Hi! Feel free to ask me anything.",
            "Greetings! What would you like to talk about?",
        ])

    # Farewell patterns
    if any(word in text for word in ["bye", "goodbye", "see you", "farewell", "take care"]):
        return random.choice([
            "Goodbye! Have a wonderful day!",
            "See you later! Feel free to come back anytime.",
            "Take care! It was nice chatting with you.",
        ])

    # Gratitude patterns
    if any(word in text for word in ["thanks", "thank you", "appreciate"]):
        return random.choice([
            "You're welcome! Let me know if there's anything else.",
            "Happy to help! Anything else you'd like to know?",
            "No problem at all! What else can I do for you?",
        ])

    # Identity / about the bot
    if any(phrase in text for phrase in ["who are you", "what are you", "your name", "about you"]):
        return (
            "I'm a simple chat assistant built with Streamlit. "
            "I don't use any external AI or APIs — my responses are generated "
            "locally with a small Python function. Pretty neat, right?"
        )

    # How-are-you patterns
    if any(phrase in text for phrase in ["how are you", "how do you do", "how's it going"]):
        return random.choice([
            "I'm just a script, but if I could feel, I'd say I'm doing great! How about you?",
            "Running smoothly! Thanks for asking. What can I help you with?",
            "All systems operational! What's on your mind?",
        ])

    # Help request
    if any(word in text for word in ["help", "assist", "support"]):
        return (
            "Sure! Here are some things you can try:\n"
            "- Ask me about **Python** or **Streamlit**\n"
            "- Say **hello** or **goodbye**\n"
            "- Ask **who I am**\n"
            "- Or just type anything and I'll do my best to reply!"
        )

    # Python-related
    if "python" in text:
        return random.choice([
            "Python is a versatile programming language known for its readability and extensive ecosystem.",
            "Python is great for web development, data science, automation, and much more!",
            "Fun fact: Python was named after Monty Python, not the snake!",
            "Python's simplicity makes it one of the best languages for beginners and experts alike.",
        ])

    # Streamlit-related
    if "streamlit" in text:
        return random.choice([
            "Streamlit makes it incredibly easy to build interactive web apps with Python!",
            "Streamlit is an open-source framework that turns Python scripts into shareable web apps.",
            "Fun fact: This entire app is built with Streamlit's chat components!",
            "Streamlit handles the frontend for you so you can focus on the logic.",
        ])

    # Joke request
    if any(word in text for word in ["joke", "funny", "laugh", "humor"]):
        return random.choice([
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "There are only 10 types of people: those who understand binary and those who don't.",
            "A SQL query walks into a bar, sees two tables, and asks: 'Can I JOIN you?'",
            "Why was the JavaScript developer sad? Because he didn't Node how to Express himself.",
        ])

    # Question patterns (fallback for questions)
    if text.endswith("?"):
        return random.choice([
            "That's a great question! Unfortunately, I'm a simple mock assistant without real knowledge.",
            "Interesting question! I'd love to give a real answer, but I'm just a local demo.",
            "I wish I could answer that properly! Try asking me about Python or Streamlit instead.",
            "Good question! As a mock assistant, I can only give simulated responses.",
        ])

    # Generic fallback
    return random.choice([
        "That's interesting! Tell me more.",
        "I see! While I'm just a mock assistant, I appreciate the conversation.",
        "Hmm, I'm not sure how to respond to that, but I'm happy to keep chatting!",
        "Fascinating! Feel free to ask me about Python, Streamlit, or just say hi!",
        "I'm a simple local assistant — no AI here! But I'll do my best to keep the conversation going.",
        "Got it! Anything else you'd like to talk about?",
    ])


# ── App header ───────────────────────────────────────────────────────────────

st.title("💬 ChatGPT-like App")
st.caption("A Streamlit chat app with mock responses — no external LLM or API used.")

# ── Session state initialization ─────────────────────────────────────────────

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! I'm your mock chat assistant. "
                "I don't use any external AI — all my replies are generated locally. "
                "Try saying **hello**, asking for a **joke**, or asking about **Python**!"
            ),
        }
    ]

# ── Display chat history ─────────────────────────────────────────────────────

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ── Handle user input ────────────────────────────────────────────────────────

if prompt := st.chat_input("Type your message here..."):
    # Append and display the user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate and display the assistant response
    response = generate_mock_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
