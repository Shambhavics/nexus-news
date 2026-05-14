import operator
from typing import Annotated,List,TypedDict 
from langchain core.messages import BaseMessage,HumanMessage,SystemMessage 
from langgraph.graph import StateGraph,END 
from langchain_ollama import chatollama