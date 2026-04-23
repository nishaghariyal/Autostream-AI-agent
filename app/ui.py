import streamlit as st
import sys
import os

# ✅ Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.agent.agent import Agent

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="AutoStream AI",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- CSS ----------
st.markdown("""
<style>

/* FULL PAGE */
html, body, .stApp {
    background-color: #020617;
    color: white;
}

/* FIX TOP SPACING (NO CUT HEADER) */
.block-container {
    padding-top: 2.5rem !important;
    max-width: 1000px;
    margin: auto;
}

/* HEADER */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #38bdf8;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 30px;
}

/* CHAT AREA */
.chat-container {
    margin-top: 20px;
}

/* USER MESSAGE */
.user-msg {
    background: linear-gradient(135deg, #22c55e, #4ade80);
    color: black;
    padding: 12px;
    border-radius: 12px;
    margin: 10px 0;
    text-align: right;
}

/* BOT MESSAGE */
.bot-msg {
    background: #1e293b;
    color: white;
    padding: 12px;
    border-radius: 12px;
    margin: 10px 0;
    text-align: left;
}

/* INPUT */
.stChatInput input {
    background-color: #0f172a !important;
    color: white !important;
    border-radius: 10px !important;
}

/* HELP BOX */
.help-box {
    text-align: center;
    background: #0f172a;
    padding: 12px;
    border-radius: 10px;
    margin-top: 30px;
    color: #cbd5f5;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="title"> AutoStream AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your Smart AI Sales Assistant</div>', unsafe_allow_html=True)

# ---------- INIT ----------
if "agent" not in st.session_state:
    st.session_state.agent = Agent()

if "chat" not in st.session_state:
    st.session_state.chat = []

if "active" not in st.session_state:
    st.session_state.active = True

# ---------- CHAT DISPLAY ----------
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for role, msg in st.session_state.chat:
    if role == "user":
        st.markdown(f'<div class="user-msg">🧑 {msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg">🤖 {msg}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- INPUT ----------
if st.session_state.active:
    user_input = st.chat_input("Type your message...")

    if user_input:
        st.session_state.chat.append(("user", user_input))

        # ✅ EXIT FIX
        if user_input.lower() == "exit":
            st.session_state.chat.append(("bot", "👋 Chat ended. Refresh to restart."))
            st.session_state.active = False
        else:
            response = st.session_state.agent.respond(user_input)
            st.session_state.chat.append(("bot", response))

        st.rerun()

# ---------- HELP ----------
st.markdown("""
<div class="help-box">
💡 <b>What you can do:</b><br>
• Ask about <b>pricing / plans</b><br>
• Ask <b>what is AutoStream</b><br>
• Type <b>i want to buy</b> to subscribe<br>
• Enter your <b>email</b> to get contacted<br>
• Type <b>exit</b> to end chat
</div>
""", unsafe_allow_html=True)