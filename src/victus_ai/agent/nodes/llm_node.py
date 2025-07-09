from langchain_community.chat_models import ChatOllama
from ..schema import GraphState

llm = ChatOllama(model="llama3:8b-instruct-q4_K_M", base_url="http://localhost:11434")

def llm_node(state: GraphState) -> GraphState:
    response = llm.invoke(state["input"])
    return {
        **state,
        "output": response.content,
        "final_answer": response.content
    }
