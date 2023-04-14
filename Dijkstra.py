from Graph import Graph
import math
INF = math.inf


def Dijkstra(origine:str , graph:Graph):
    summits={}
    path ={}
    queue =[]
    summits[origine] = 0 
    for summit in graph.getSummits():
        if summit != origine:
            summits[summit] = INF
    while len(queue) <= graph.size():
        
    
        


