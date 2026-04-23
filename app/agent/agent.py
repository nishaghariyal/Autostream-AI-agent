from app.intent.intent_classifier import detect_intent
from app.rag.rag_pipeline import generate_answer
import re
import json
import os


# =============================
# ✅ SAVE LEAD FUNCTION (FIXED)
# =============================
def save_lead(new_lead):
    file_path = "leads.json"   # 🔥 use correct path

    # Create file if not exists
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump([], f)

    # Read existing data
    with open(file_path, "r") as f:
        data = json.load(f)

    # Add new lead
    data.append(new_lead)

    # Save back
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


# =============================
# 🤖 AGENT CLASS
# =============================
class Agent:
    def __init__(self):
        self.last_intent = None

        # 🔥 Lead capture state
        self.lead_stage = None
        self.lead_data = {}

    # =============================
    # ✅ VALIDATIONS
    # =============================

    def is_email(self, text):
        return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", text)

    def is_valid_name(self, text):
        return len(text.strip()) >= 3 and text.isalpha()

    # =============================
    # ✅ MOCK API (FIXED)
    # =============================

    def mock_lead_capture(self, name, email, platform):
        print(f"Lead captured successfully: {name}, {email}, {platform}")

        # ✅ Proper JSON save
        new_lead = {
            "name": name,
            "email": email,
            "platform": platform
        }

        save_lead(new_lead)

    # =============================
    # 🧠 MAIN RESPONSE FUNCTION
    # =============================

    def respond(self, user_input):
        user_input = user_input.strip()

        if not user_input:
            return "🙂 Please enter something."

        # 🔥 EXIT HANDLING
        if user_input.lower() == "exit":
            return "👋 Chat ended. Thank you!"

        # =============================
        # 🔥 LEAD FLOW HANDLING
        # =============================

        # STEP 1: NAME
        if self.lead_stage == "name":
            if not self.is_valid_name(user_input):
                return "⚠️ Please enter a valid name (at least 3 letters, no numbers)."

            self.lead_data["name"] = user_input
            self.lead_stage = "email"
            return "📧 Please enter your email"

        # STEP 2: EMAIL
        if self.lead_stage == "email":
            if not self.is_email(user_input):
                return "⚠️ Please enter a valid email (example: name@gmail.com)"

            self.lead_data["email"] = user_input
            self.lead_stage = "platform"
            return "📱 Which platform do you use? (YouTube / Instagram etc.)"

        # STEP 3: PLATFORM
        if self.lead_stage == "platform":
            self.lead_data["platform"] = user_input

            # 🔥 CALL TOOL
            self.mock_lead_capture(
                self.lead_data["name"],
                self.lead_data["email"],
                self.lead_data["platform"]
            )

            # 🔥 RESET STATE
            self.lead_stage = None
            self.lead_data = {}
            self.last_intent = None   # ✅ reset memory

            return "✅ Thanks! Your details are submitted. Our team will contact you soon."

        # =============================
        # 🔥 INTENT DETECTION
        # =============================

        intent = detect_intent(user_input)

        # 🔥 CONTEXT MEMORY (SMART FLOW)
        if intent == "other" and self.last_intent == "pricing":
            if user_input.lower() in ["ok", "yes", "sounds good"]:
                intent = "high_intent"

        self.last_intent = intent

        # =============================
        # 🔥 RESPONSES
        # =============================

        if intent == "greeting":
            return "Hi! Welcome to AutoStream 🚀 How can I help you?"

        elif intent == "pricing":
            return generate_answer(user_input)

        elif intent == "high_intent":
            self.lead_stage = "name"
            return "🔥 Great choice! Let's get you started.\n\n👤 Please tell me your name."

        elif intent == "about":
            return generate_answer(user_input)

        elif intent == "support":
            return generate_answer(user_input)

        elif intent == "casual":
            return "😊 Got it! Let me know how I can help."

        else:
            return generate_answer(user_input)