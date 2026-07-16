#Using LLM is not preffered, use chatmodels instead as they are optimized and better for conversation, as directed itself by LangChain

#here is just an example of the code, it will not run since I do not own any open-ai API key

from langchain_openai import openAi
from dotenv import load_dotenv

load_dotenv()

llm = OpenAi(model = 'gpt-3.5-turbo-instruct')

result = invoke("What  is the capital of India")

print(result);

#we receive - New Delhi is the capital of India