from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("HF_TOKEN")

print("Token loaded:", token is not None)

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    provider="featherless-ai",
    huggingfacehub_api_token=token
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Who is the Prime Minister of India?")

print(result.content)