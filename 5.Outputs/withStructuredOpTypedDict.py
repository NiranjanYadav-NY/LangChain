from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash"
)

#schema
class Review(TypedDict):
    key_themes :  Annotated[list[str], "Write down all the key themes of the discussed int the review"]
    summary:Annotated[str, "A brief summary of the review"] 
    sentiment: Annotated[str, "Return sentinment of the reivew either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]], "write down all the pros inside the list"]
    cons: Annotated[Optional[list[str]], "write down all the cons inside the list"]

structured_model =  model.with_structured_output(Review)


result = structured_model.invoke("""A great restaurant review highlights the food, service, and atmosphere. Use this specific, plug-and-play template. Just swap the bracketed words to fit your meal.
"Hands down, one of the best meals I have had recently ! I visited FNC Restaurant  in City for dinner. The Signature Dish was cooked to
absolute perfection. The flavors were fresh and perfectly balanced.The staff made the experience even better. Our server was fast, kind, and gave great recommendations. The atmosphere
was cozy and welcoming—ideal for a family dinner""")

print(result)
print(result['summary'])
print(result['sentiment'])