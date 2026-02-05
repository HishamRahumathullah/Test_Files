from langgraph.graph import StateGraph, START, END
from typing import TypedDict


class AgentState(TypedDict):
    no1: int
    no2: int
    op1: str
    no3: int
    no4: int
    op2: str
    result: int


def fisrt_add(state: AgentState) -> AgentState:
    state["result"] = state["no1"] + state["no2"]
    return state


def first_sub(state: AgentState) -> AgentState:
    state["result"] = state["no1"] - state["no2"]
    return state


def fisrt_op(state: AgentState) -> AgentState:
    if state["op1"] == "+":
        return "first_addition"
    elif state["op1"] == "-":
        return "first_subtraction"
    else:
        raise ValueError("Invalid operation in first operation")


def second_add(state: AgentState) -> AgentState:
    state["result"] = state["result"] + state["no3"] + state["no4"]
    return state


def second_sub(state: AgentState) -> AgentState:
    state["result"] = state["result"] - state["no3"] - state["no4"]
    return state


def second_op(state: AgentState) -> AgentState:
    if state["op2"] == "+":
        return second_add(state)
    elif state["op2"] == "-":
        return second_sub(state)
    else:
        raise ValueError("Invalid operation in second operation")


graph = StateGraph(AgentState)
graph.add_node("first_add", fisrt_add)
graph.add_node("first_sub", first_sub)
graph.add_node("first_op", lambda state: state)

graph.add_edge(START, "first_op")
graph.add_conditional_edges(
    "first_op",
    fisrt_op,
    {"first_addition": "first_add", "first_subtraction": "first_sub"},
)

graph.add_edge("first_add", END)
graph.add_edge("first_sub", END)

app = graph.compile()
