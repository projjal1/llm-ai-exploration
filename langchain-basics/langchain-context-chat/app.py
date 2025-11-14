from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage

model = init_chat_model("llama3:8b", model_provider="ollama")

msgs = ['Hi I am Projjal', 'What is my name?']

# It cannot recall previous chats
# for m in msgs:
#     print(f'Question: {m}')
#     print(f'Answer: {model.invoke([HumanMessage(content=m)]).content}')
#     print('*' * 10)


# Able to recall if fixed thread is there
# print(model.invoke(
#     [
#         HumanMessage(content="Hi! I'm Projjal"),
#         AIMessage(content="Hello Projjal! How can I assist you today?"),
#         HumanMessage(content="What's my name?"),
#     ]
# ).content)


# Building in memory persistence layer
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

# Define a new graph
workflow = StateGraph(state_schema=MessagesState)


# Define the function that calls the model
def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}


# Define the (single) node in the graph
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# Add memory
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

# Define a custom thread ID
thread_id = "chat1234"
config = {"configurable": {"thread_id": thread_id}}

updated_msgs = ['Hi I am Projjal and I live in Sweden', 'What is my name?', 'I am a software engineer', 'Suggest me 2 ways to grow in my job', 'Which 2 top industry is most profitable in my country?']

# Let us repeat our initial workflow with current memory context
for m in updated_msgs:
    print(f'Question: {m}')
    input_messages = [HumanMessage(m)]
    output = app.invoke({"messages": input_messages}, config)
    print(f'Answer: {output["messages"][-1].content}')
    print('*' * 10)