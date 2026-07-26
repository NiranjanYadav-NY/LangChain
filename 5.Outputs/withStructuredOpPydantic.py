from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

class Review(BaseModel):
    key_themes: list[str] = Field(
        description="Write down all the key themes discussed in the review."
    )

    summary: str = Field(
        description="A brief summary of the review."
    )

    sentiment: Literal["positive", "negative", "neutral"] = Field(
        description="Return the sentiment of the review."
    )

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
Hands down, one of the best meals I have had recently!
I visited FNC Restaurant in City for dinner.

The Signature Dish was cooked to absolute perfection.
The flavors were fresh and perfectly balanced.

The staff made the experience even better.
Our server was fast, kind, and gave great recommendations.

The atmosphere was cozy and welcoming—ideal for a family dinner.
""")

print(result)
print(result.summary)
print(result.sentiment)