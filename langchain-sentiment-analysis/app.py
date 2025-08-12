from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model

llm = init_chat_model("mistral:7b", model_provider="ollama")

template = """
Extract the desired information from the following passage, think deeply.
Only extract the properties mentioned in the 'Classification' function.
Passage:
{input}
"""

tagging_prompt = ChatPromptTemplate.from_template(template)

class Classification(BaseModel):
    sentiment: str = Field(..., enum=["happy", "angry", "sad"])
    language: str = Field(...,
        description="The language the text is written in",
        enum=["Spanish", "English"])


# Structured LLM
structured_llm = llm.with_structured_output(Classification)

# Input prompt
statements = [
    "Estoy muy enojado con vos! Te voy a dar tu merecido!",
    "Estoy increiblemente contento de haberte conocido! Creo que seremos muy buenos amigos!",
    "Weather is ok here, I can go outside without much more than a coat",
    "I will get my revenge against him for damaging my car"
]

for stmt in statements:
    # Invoke the prompt
    prompt = tagging_prompt.invoke({"input": stmt})
    # Invoke prompt to llm
    response = structured_llm.invoke(prompt)

    print(response.model_dump())