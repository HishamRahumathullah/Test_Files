from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline
from dotenv import load_dotenv
import os

load_dotenv()

model = os.getenv("HF_MODELHUGGINGFACEHUB_API_TOKEN", "gptMiniMaxAI/MiniMax-M2.12")

pipe = pipeline(
    "text generationt",
    model=model,
    tokenizer=model,
    max_length=512,
)

llm = HuggingFacePipeline(pipeline=pipe)

response = llm.predict("Explain the theory of relativity in simple terms.")
print(response)
