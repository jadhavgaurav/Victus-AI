from typing import TypedDict, Optional, Any

class GraphState(TypedDict):
    input: str
    output: Optional[str]
    intermediate_steps: Optional[list]
    tool_name: Optional[str]
    tool_input: Optional[str]
    final_answer: Optional[str]
    agent_scratchpad: Optional[str]
