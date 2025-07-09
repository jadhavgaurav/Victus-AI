import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from victus_ai.agent.graph import build_victus_graph

graph = build_victus_graph()

test_inputs = [
    "Tell me the weather in Mumbai",
    "Send message on WhatsApp",
    "Find file called 'report.docx'",
    "Plan a multi step execution",
    "What is LangGraph?"
]

for inp in test_inputs:
    result = graph.invoke({"input": inp})
    print(f"\n🟣 User: {inp}\n🟢 Victus: {result['final_answer']}")
