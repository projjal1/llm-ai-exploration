from typing import List, Optional
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model

# Pydantic model
# Single person
class Person(BaseModel):
    """Information about a person."""
    # ^ Doc-string for the entity Person.
    # This doc-string is sent to the LLM as the description of the schema Person,
    # and it can help to improve extraction results.

    # Note that:
    # 1. Each field is an `optional` -- this allows the model to decline to extract it!
    # 2. Each field has a `description` -- this description is used by the LLM.
    # Having a good description can help improve extraction results.
    name: Optional[str] = Field(default=None, description="The name of the person")
    hair_color: Optional[str] = Field(
        default=None, description="The color of the person's hair"
    )
    height_in_meters: Optional[str] = Field(
        default=None, description="Height value measured in meters, no formula"
    )

# List of persons
class Data(BaseModel):
    """Extracted data about people."""

    # Creates a model so that we can extract multiple entities.
    people: List[Person]

# Define a custom prompt to provide instructions and any additional context.
prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert extraction algorithm. "
            "Only extract name, hair color and tall/height in meters (convert from feet) from the text."
            "If you do not know the value of an attribute asked to extract, "
            "return null for the attribute's value.",
        ),
        ("human", "{text}"),
    ]
)

# define model
llm = init_chat_model("mistral:7b", model_provider="ollama")
structured_llm = llm.with_structured_output(schema=Person)
text = "Alan Smith is 6 feet tall height and has blond hair color."
prompt = prompt_template.invoke({"text": text})
print(structured_llm.invoke(prompt))

structured_llm = llm.with_structured_output(schema=Data)
text = "My name is Jeff, my hair is red and i am 6 feet tall height. Anna has the same hair color as Jeff."
prompt = prompt_template.invoke({"text": text})
print(structured_llm.invoke(prompt))