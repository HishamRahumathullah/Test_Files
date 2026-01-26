import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

# Set token
load_dotenv()

if not os.getenv("HUGGINGFACEHUB_API_TOKEN"):
    raise ValueError("API token is not found in env file ")


# Create LLM backend first
llm_backend = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    max_new_tokens=512,
    temperature=0.7,
)

# Wrap with ChatHuggingFace for proper chat formatting
chat_model = ChatHuggingFace(llm=llm_backend)

while True:
    user_input = input("Ask anything (or 'quit' to exit): ")

    if user_input == "quit":
        print("Goodbye!")
        break

    # Use chat format (list of messages)
    messages = [
        ("system", "You are a helpful teacher."),
        ("human", user_input),
    ]

    try:
        response = chat_model.invoke(messages)
        print("Assistant : ", response.content)  # Access the content attribute
    except Exception as e:
        print(f" Error {e}")
