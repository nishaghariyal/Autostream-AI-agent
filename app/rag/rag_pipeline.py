import json
from app.config import call_llm

# ✅ Load JSON (RAG source)
with open("data/knowledge.json", "r") as f:
    data = json.load(f)


# ✅ Retrieve context (RAG logic)
def retrieve_context(query):
    query = query.lower()

    # Pricing context
    if any(w in query for w in ["price", "pricing", "plan", "cost"]):
        return f"""
💰 Pricing Plans:

Basic Plan:
{data['pricing']['basic']}

Pro Plan:
{data['pricing']['pro']}
"""

    # About context
    if "autostream" in query:
        return data["features"]["autostream"]

    # Policies (NEW 🔥)
    if any(w in query for w in ["refund", "support", "policy"]):
        return f"""
📜 Policies:

Refund: {data['policies']['refund']}
Support: {data['policies']['support']}
"""

    return None  # IMPORTANT: return None instead of string
    


# ✅ Generate answer (FINAL FUNCTION)
def generate_answer(query):
    query = query.lower().strip()

    # 🔥 Handle small talk (IMPORTANT FIX)
    if query in ["ok", "yes", "no", "hmm"]:
        return "😊 Got it! How can I help you?"

    # 🔥 Direct response (fast + no API)
    if any(w in query for w in ["price", "pricing", "plan", "cost"]):
        return f"""💰 Pricing Plans:

Basic: {data['pricing']['basic']}
Pro: {data['pricing']['pro']} 🚀
"""

    # 🔥 About response (no API needed)
    if "autostream" in query:
        return data["features"]["autostream"]

    # 🔥 Policies (NEW)
    if any(w in query for w in ["refund", "support", "policy"]):
        return f"""
📜 Policies:

Refund: {data['policies']['refund']}
Support: {data['policies']['support']}
"""

    # 🔥 Use RAG + AI (only if needed)
    context = retrieve_context(query)

    # ❌ If no context → don't call API (IMPORTANT FIX)
    if not context:
        return "😊 I can help with pricing, plans, or subscriptions!"

    prompt = f"""
Answer the user based on the context below.

Context:
{context}

Question:
{query}
"""

    try:
        return call_llm(prompt)

    except Exception as e:
        print("RAG Error:", e)
        return "⚠️ AI not available right now."