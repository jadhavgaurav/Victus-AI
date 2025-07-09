from ..schema import GraphState

def agent_node(state: GraphState) -> GraphState:
    # For now, mock agent execution
    return {
        **state,
        "output": f"Agent reasoning completed for: {state['input']}",
        "final_answer": f"Agent reasoning completed for: {state['input']}"
    }
