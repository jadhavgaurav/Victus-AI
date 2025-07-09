from ..schema import GraphState

def tool_node(state: GraphState) -> GraphState:
    # For now, mock tool execution
    return {
        **state,
        "output": f"Tool executed for input: {state['input']}",
        "final_answer": f"Tool executed for input: {state['input']}"
    }
