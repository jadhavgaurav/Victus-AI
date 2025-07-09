from langgraph.graph import StateGraph, END
from .schema import GraphState
from .nodes.llm_node import llm_node
from .nodes.tool_node import tool_node
from .nodes.agent_node import agent_node

# 🧠 Routing logic (not a real node)
def router_node(state: GraphState) -> str:
    user_input = state["input"].lower()
    if "weather" in user_input:
        return "tool"
    elif "whatsapp" in user_input or "send message" in user_input:
        return "tool"
    elif "find file" in user_input or "search" in user_input:
        return "tool"
    elif "plan" in user_input or "multi step" in user_input:
        return "agent"
    else:
        return "llm"

# ✅ Dummy passthrough node just to trigger router
def router_passthrough(state: GraphState) -> GraphState:
    return state

def build_victus_graph():
    builder = StateGraph(GraphState)

    builder.add_node("router", router_passthrough)
    builder.add_node("llm", llm_node)
    builder.add_node("tool", tool_node)
    builder.add_node("agent", agent_node)

    # ✅ Declare entry point
    builder.set_entry_point("router")

    # ✅ Conditional routing based on logic
    builder.add_conditional_edges(
        "router",
        router_node,
        {
            "llm": "llm",
            "tool": "tool",
            "agent": "agent"
        }
    )

    builder.add_edge("llm", END)
    builder.add_edge("tool", END)
    builder.add_edge("agent", END)

    return builder.compile()
