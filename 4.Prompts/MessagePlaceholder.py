from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash"
)
#chat template
chat_template = ChatPromptTemplate([
    ('system', 'You ate a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history')
    ('human', '{query}')
])

#load chat history

chat_history = []
with open('chat_history.text') as f:
    chat_history.extend(f.readlines())

print(chat_history)

#create prompts
prompt = chat_template.invoke({'chat_history': chat_history,
                     'query': 'where is my refund'
                    })
print(prompt)