from Graph import Graph
import math
INF = math.inf

TestGraph=Graph(graph={"s":{"t":10,"y":5},"t":{"x":1,"y":2},"y":{"t":3,"z":2,"x":9},"x":{"z":4},"z":{"x":4,"s":7}})



def Dijkstra(origine:str , graph:Graph):
    summits={}
    
    path ={}
    queue=graph.getSummits()
    summits[origine] = 0 
    for summit in graph.getSummits():
        if summit != origine:
            summits[summit] = INF

    while queue!=[]:
        u = extraireMin(queue,summits)
        neighbours = graph.getNeigbours(u)
        for adj in neighbours:
            distance=summits[u]+ graph.getWeight(u,adj)
            if summits[adj]>distance:
                summits[adj]=distance
                path[u]=adj 
                
    return path
                
    # for summit in graph.getSummits:
    #     if  summit not in queue:
    #         neighbours = graph.getNeigbours(summit)
            
    #         for neighbour in neighbours:
    #             distance=summits[summit]+ graph.getWeight(summit,neighbour)
    #             if summits[neighbour]>distance:
    #                 summits[neighbour] = distance
    #                 if summits[min]>summits[neighbour]:
    #                     min = neighbour
            
            
                
def extraireMin(queue:list,summits:dict):
    
    if queue != []:
        values=list(summits.values())
        
        sorted(values)
        print(queue)
        key=""
        for summit in summits:
            if values[0] == summits[summit]:
                key = str(summit)
        indexA = queue.index(key)
        exchange(queue,0,indexA)
        
    else: 
        print("queue is empty!!")    
    return queue.pop(0)
    
def exchange(list,indexA,indexB):
    list[indexA], list[indexB] = list[indexB], list[indexA]


        
############### TEST##################
print(Dijkstra("s",TestGraph))
    



    
        


