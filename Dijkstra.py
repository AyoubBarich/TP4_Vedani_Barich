from Graph import Graph
import math
INF = math.inf


def Dijkstra(origine:str , graph:Graph):
    summits={}
    path ={}
    queue =[]
    summits[origine] = 0 
    for summit in graph.getSummits:
        if summit != origine:
            summits[summit] = INF
    for summit in graph.getSummits:
        if  summit not in queue:
            neighbours = graph.getNeigbours(summit)
            min = neighbours[0]
            for neighbour in neighbours:
                distance=summits[summit]+ graph.getWeight(summit,neighbour)
                if summits[neighbour]>distance:
                    summits[neighbour] = distance
                    if summits[min]>summits[neighbour]:
                        min = neighbour
            
            
                



    
        


