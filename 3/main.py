# This is the code for run locally

from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
from transformers import BitsAndBytesConfig

# Step 1: Load model with quantization (saves GPU memory)
nf4_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=torch.bfloat16,
)

model_id = "microsoft/DialoGPT-medium"  # Free 345M parameter model

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, quantization_config=nf4_config, device_map="auto"
)

# Step 2: Create Hugging Face pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=512,
    temperature=0.7,
)

# Step 3: Wrap with LangChain
llm = HuggingFacePipeline(pipeline=pipe)

# Step 4: Use it like any LangChain LLM
prompt = PromptTemplate.from_template("Write a short story about {topic}")
chain = prompt | llm

result = chain.invoke({"topic": "a robot learning to paint"})
print(result)
