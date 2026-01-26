import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()


try:
    api_key = os.environ["HUGGINGFACEHUB_API_TOKEN"]
except KeyError:
    raise EnvironmentError(
        "Missing HUGGINGFACEHUB_API_TOKEN. "
        "Run: export HUGGINGFACEHUB_API_TOKEN='your_key'"
    ) from None

client = InferenceClient(api_key)

MODEL_NAME = "moonshotai/Kimi-K2-Thinking"

while True:
    try:
        user_input = input("You: ").strip()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        break

    # Skip empty input
    if not user_input:
        continue

    # Exit command
    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    # Call API with error handling
    try:
        print("🤔 Thinking...", end="\r", flush=True)

        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": user_input}],
        )

        response = completion.choices[0].message.content
        print(f"Bot: {response}\n")  # ✅ Works but needs newline for readability

    except Exception as e:
        print(f"\n❌ Error: {type(e).__name__}: {e}")
        print("   → Check your API key, model name, and internet connection.\n")
