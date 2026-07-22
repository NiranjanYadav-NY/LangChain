from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-Flash"
)

chat_template = ChatPromptTemplate.from_messages([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms and in short, what is {topic}')
])

prompt = chat_template.invoke({'domain': 'cricket',
                               'topic':'Dusra'})
result = model.invoke(prompt)
print(result.content)