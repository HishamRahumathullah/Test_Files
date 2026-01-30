from typing import TypedDict
from langgraph.graph import StateGraph 

class AgentState(TypedDict):
    name:str
    age : str
    skills :list[str]
    result: str
    
def fst_node(state:AgentState) -> AgentState:
        state['name'] = input("Enter your name : ")
        state['result'] =f" Hi { state['name']}"
        return state

def snd_node(state:AgentState) ->AgentState :
        state['age'] = input("Enter your age : ")
        state['result'] += f", your age is {state['age']} years and "
        return state
def trd_node(state:AgentState) ->AgentState :
        state["skills"] = input("Enter your skills  : ")
        
        state['result'] += f" you have {(state['skills'])} skills"
        return state    
    
graph= StateGraph(AgentState)
graph.add_node("fst_node",fst_node)
graph.add_node("snd_node",snd_node)
graph.add_node("trd_node",trd_node)

graph.set_entry_point("fst_node")
graph.add_edge("fst_node","snd_node")
graph.add_edge("snd_node","trd_node")
graph.set_finish_point("trd_node")

app = graph.compile()
res = app.invoke({'name':'', 'age':'', 'skills':"", 'result':''})
print(res['result'])
