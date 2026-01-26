import sys

print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")

try:
    import langchain

    print(f"✅ LangChain version: {langchain.__version__}")
    print(f"Location: {langchain.__file__}")
except ImportError:
    print("❌ LangChain NOT found")

try:
    from langchain.prompts import PromptTemplate

    print("✅ PromptTemplate import works")
except ImportError as e:
    print(f"❌ Import failed: {e}")
