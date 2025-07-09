from ..schema import GraphState

def router_node(state: GraphState) -> str:
    user_input = state["input"].lower()

    if "weather" in user_input:
        return "tool"
    elif "send message" in user_input or "whatsapp" in user_input:
        return "tool"
    elif "search" in user_input or "find file" in user_input:
        return "tool"
    elif "plan" in user_input or "multi step" in user_input:
        return "agent"
    else:
        return "llm"
