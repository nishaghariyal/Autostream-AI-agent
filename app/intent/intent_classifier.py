from app.config import call_llm

def detect_intent(user_input):
    text = user_input.lower().strip()

    # ✅ GREETING
    if any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"

    # ✅ PRICING
    elif any(word in text for word in ["price", "pricing", "plan", "cost"]):
        return "pricing"

    # 🔥 IMPROVED HIGH INTENT (IMPORTANT FOR ASSIGNMENT)
    elif any(word in text for word in [
        "buy", "subscribe", "purchase",
        "sign up", "get started", "start now",
        "interested", "want this", "need this",
        "take plan", "i will take", "i want this"
    ]):
        return "high_intent"

    # ✅ SUPPORT / POLICY
    elif any(word in text for word in ["refund", "support", "policy"]):
        return "support"

    # ✅ ABOUT
    elif any(word in text for word in ["autostream", "what is", "about"]):
        return "about"

    # ✅ CASUAL (VERY IMPORTANT FIX)
    elif text in ["ok", "yes", "no", "hmm", "thanks", "okay", "fine"]:
        return "casual"

    # 🔥 SMALL INPUT → DO NOT CALL API
    if len(text.split()) <= 2:
        return "other"

    # 🔥 AI FALLBACK (ONLY WHEN NEEDED)
    prompt = f"""
Classify the user intent into ONE word:
greeting, pricing, high_intent, support, about, casual, other

User: {user_input}
Answer only one word.
"""

    try:
        response = call_llm(prompt)

        intent = response.strip().lower()

        allowed = [
            "greeting", "pricing", "high_intent",
            "support", "about", "casual", "other"
        ]

        if intent in allowed:
            return intent
        else:
            return "other"

    except Exception as e:
        print("Intent Error:", e)
        return "other"