from langchain_community.document_loaders import WebBaseLoader
from langchain.chat_models import init_chat_model
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.llm import LLMChain
from langchain_core.prompts import ChatPromptTemplate

# Load documents from a web page
loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent")
docs = loader.load()

# Initialize a chat model
llm = init_chat_model("llama3:8b", model_provider="ollama")

# Define prompt
prompt = ChatPromptTemplate.from_messages(
    [("system", "Write a concise summary of the following:\\n\\n{context}")]
)

# Instantiate chain
chain = create_stuff_documents_chain(llm, prompt)

# Invoke chain
for token in chain.stream({"context": docs}):
    print(token, end="", flush=True)