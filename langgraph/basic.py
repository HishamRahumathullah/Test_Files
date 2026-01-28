from langgraph.graph import StateGraph,END
from typing import Dict,TypedDict

class get_response (TypedDict):
    message : str
    
def test_basic (state :get_response) -> get_response:
    state["message"] = input("Enter your name: ")
    state["message"] = f"Hello, {state['message']} how are you?"
    return state

graph = StateGraph(get_response)

graph.add_node("test", test_basic)
graph.set_entry_point("test")
graph.add_edge("test",END)

app = graph.compile()
result=app.invoke({"message":""})
print(result)

    