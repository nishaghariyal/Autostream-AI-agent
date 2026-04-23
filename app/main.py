from app.agent.agent import Agent

def run():
    agent = Agent()

    print("🚀 AutoStream AI Agent Started (type 'exit' to quit)\n")

    # ✅ Suggestions for user (YOU ASKED THIS)
    print("💡 Try asking:")
    print("- pricing")
    print("- plans")
    print("- what is autostream\n")

    while True:
        user_input = input("You: ")

        # exit condition
        if user_input.lower() == "exit":
            print("👋 Exiting AutoStream AI Agent. Goodbye!")
            break

        # empty input handling
        if not user_input.strip():
            print("Agent: Please enter something 😊")
            continue

        try:
            response = agent.respond(user_input)
            print("Agent:", response)

        except Exception as e:
            print("❌ Error:", e)
            print("Agent: Something went wrong, please try again.")

if __name__ == "__main__":
    run()