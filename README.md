🤖 AutoStream AI Agent

Social-to-Lead Agentic Workflow

---

🚀 Project Overview

AutoStream AI Agent is a conversational AI system designed to convert social media conversations into qualified business leads.

---

🌐 Live Demo

👉 Try the app here:
https://autostream-ai-agent.streamlit.app/

---

🎯 Features

✅ Intent Detection (rule-based + optional LLM fallback)
✅ RAG-based Knowledge Retrieval using local JSON
✅ High-Intent User Detection (ready to sign up)
✅ Multi-step Lead Capture (Name → Email → Platform)
✅ Mock API Execution for lead storage
✅ Context Awareness (conversation memory)
✅ Streamlit-based Chat UI

---

🧠 Agent Workflow

1. User interacts with agent
2. Agent detects intent
3. If query → uses RAG (knowledge.json)
4. If high intent → triggers lead capture flow
5. Collects:
   - Name
   - Email
   - Platform
6. Calls:
   mock_lead_capture(name, email, platform)
7. Stores lead data locally

---

🔍 Intent Types

- Greeting
- Pricing / Product Inquiry
- High Intent (Buy / Subscribe)
- Support / Policy
- About Product
- Casual

---

📊 High Intent Detection

High intent is detected using:

- Keywords: buy, subscribe, get started, interested
- Context: user agreeing after pricing

Example:

User: Tell me pricing
User: That sounds good
→ Detected as HIGH INTENT

---

🗂️ Project Structure

app/
│
├── agent/
│   └── agent.py
│
├── intent/
│   └── intent_classifier.py
│
├── rag/
│   └── rag_pipeline.py
│
├── config.py
├── main.py
├── ui.py

data/
└── knowledge.json

leads.json
requirements.txt
README.md

---

📚 Knowledge Base (RAG)

Stored in:

data/knowledge.json

Includes:

- Pricing Plans
- Policies
- Product Info

---

⚙️ Tech Stack

- Language: Python 3.9+
- Framework: Streamlit
- LLM: OpenRouter / GPT / Gemini (optional fallback)
- Architecture: Agentic Workflow

---

🧪 How to Run

1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Run CLI Agent
python -m app.main

3️⃣ Run UI
streamlit run app/ui.py

---

💬 Example Conversation

User: Hi
Agent: Welcome to AutoStream 🚀

User: Tell me pricing
Agent: Shows pricing plans

User: I want to buy
Agent: Please tell me your name

User: John
Agent: Enter your email

User: john@gmail.com
Agent: Which platform do you use?

User: YouTube

→ Lead captured successfully

---

🔧 Tool Execution

def mock_lead_capture(name, email, platform):
print(f"Lead captured successfully: {name}, {email}, {platform}")

---

🧠 State Management

- Last intent
- Lead capture stage
- Partial user data

---

📌 Deliverables Covered

✔ Agent Logic
✔ RAG Pipeline
✔ Intent Classification
✔ Tool Execution
✔ UI Interface

---

🚀 Future Improvements

- Database integration
- Dashboard for leads
- Voice input
- Advanced UI
- LLM fine-tuning

---

👩‍💻 Author

Nisha Ghariyal

---

⭐ Conclusion

This project demonstrates how a Conversational AI Agent can:

- Understand user intent
- Provide accurate answers
- Identify potential customers
- Capture leads automatically

Making it a real-world AI-powered sales assistant.


📱 WhatsApp Deployment (Webhook Integration)

To integrate the AutoStream AI Agent with WhatsApp, we can use the WhatsApp Business API along with Webhooks.

---

🧠 Architecture Overview

1. User sends a message on WhatsApp
2. WhatsApp sends this message to our backend via a Webhook
3. Our backend processes the message using the AI Agent
4. The agent generates a response
5. The response is sent back to the user via WhatsApp API

---

⚙️ Implementation Steps

1️⃣ Setup WhatsApp Business API

- Use Meta WhatsApp Cloud API or providers like Twilio
- Register a WhatsApp Business account

2️⃣ Create a Webhook Endpoint

- Build a backend using FastAPI / Flask
- Example endpoint:

from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def webhook(req: Request):
    data = await req.json()
    user_message = data["message"]

    # Pass message to agent
    response = agent.respond(user_message)

    # Send response back to WhatsApp API
    return {"reply": response}

---

3️⃣ Connect Webhook to WhatsApp

- Add your webhook URL in Meta Developer Dashboard
- Verify webhook using token

---

4️⃣ Send Message Back to User

- Use WhatsApp Cloud API:

import requests

def send_message(phone, text):
    url = "https://graph.facebook.com/v18.0/PHONE_NUMBER_ID/messages"
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": phone,
        "text": {"body": text}
    }
    requests.post(url, headers=headers, json=data)

---

🔄 Final Flow

User → WhatsApp → Webhook → AI Agent → Response → WhatsApp → User

---

🚀 Advantages

- Real-time communication
- Works on mobile (high engagement)
- Scalable for business automation
- Can capture leads directly from chat

---

📌 Future Improvements

- Store leads in database
- Add chatbot menu / buttons
- Integrate CRM tools
- Add analytics dashboard

---

✅ Conclusion

By using Webhooks and WhatsApp Cloud API, this AI agent can be deployed as a real-world conversational assistant capable of capturing leads directly from WhatsApp chats.


--------------------------------------------------------

🧠 Architecture Explanation

This project follows an agentic workflow design inspired by frameworks like LangGraph and AutoGen, where the system is structured as a sequence of intelligent steps rather than a single response generator. I chose this approach because it enables better control over conversation flow, modularity, and real-world task execution such as lead capture.

Instead of relying fully on an LLM, the agent combines rule-based intent detection with Retrieval-Augmented Generation (RAG). This ensures faster responses, lower cost, and more predictable behavior while still allowing scalability to integrate LLMs if needed.

State management is handled within the Agent class using internal variables such as "last_intent", "lead_stage", and "lead_data". These variables allow the system to maintain context across multiple conversation turns (typically 5–6 turns). For example, when a user shows high intent, the agent transitions into a structured lead capture flow, sequentially collecting name, email, and platform without losing context.

This design mimics how LangGraph manages node transitions and state persistence, ensuring that each step in the conversation is context-aware and goal-driven. Overall, the architecture is modular, extensible, and suitable for real-world conversational AI applications.
