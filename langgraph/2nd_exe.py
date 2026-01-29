from langgraph.graph import StateGraph
from typing import TypedDict, List, Any

class AgentState(TypedDict):
    name:str
    value: List[int]
    op: str
    result:float

def agent_func(state:AgentState) -> AgentState:
    state['name']= input("Enter your name :  ")
    num = input ("Enter numbers seperated by commas : ").split(",")
    state["value"] = [float(x.strip()) for x in num]
    state['op']= input("Enter operation (+ or *): ")
    
    length= len(state['value'])
    state["result"]= 0 if state["op"]=="+" else 1   
    for i in range (length):
        
        if state["op"] == "+":
                state["result"]=state["result"] + state["value"][i]
        elif state["op"] =="*":
            state["result"]=state["result"] * state["value"][i]
        else:
            print("Invalid operation") 
    print(f"hello {state['name']}, the result is {state['result']}")              
    return state     

graph = StateGraph(AgentState)
graph.add_node("func",agent_func)
graph.set_entry_point("func")
graph.set_finish_point("func")

app=graph.compile()
result = app.invoke({"name":"", "value":[], "op" :"", "result":0 })
# print(result["result"])  