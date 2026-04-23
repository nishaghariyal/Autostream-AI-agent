🤖 AutoStream AI Agent

Social-to-Lead Agentic Workflow

---

🚀 Project Overview

AutoStream AI Agent is a conversational AI system designed to convert social media conversations into qualified business leads.

This project demonstrates a real-world GenAI workflow including:

- Intent Detection
- RAG (Retrieval-Augmented Generation)
- High-Intent Lead Identification
- Lead Capture (Tool Execution)

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
│
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
- Architecture: Agentic Workflow (Rule-based + RAG + Tool Execution)

---

🧪 How to Run

1️⃣ Install Dependencies

pip install -r requirements.txt

2️⃣ Run CLI Agent

python -m app.main

3️⃣ Run UI (Recommended)

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

⚠️ Triggered only after collecting all details

---

🧠 State Management

The agent maintains:

- Last intent
- Lead capture stage
- Partial user data

Ensures smooth multi-turn conversation (5–6 turns)

---

📌 Deliverables Covered

✔ Agent Logic
✔ RAG Pipeline
✔ Intent Classification
✔ Tool Execution
✔ UI Interface
✔ requirements.txt
✔ README.md

---

🚀 Future Improvements

- Database integration (SQLite / MongoDB)
- Dashboard for leads
- Voice input (speech-to-text)
- Advanced UI (chat animations)
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

---