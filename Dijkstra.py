from Graph import Graph
from Graph import Couple
import math
from Heap import Heap
INF = math.inf


TestGraph = Graph(graph={"s": {"t": 10, "y": 5}, "t": {"x": 1, "y": 2}, "y": {
                  "t": 3, "z": 2, "x": 9}, "x": {"z": 4}, "z": {"x": 6, "s": 7}})



def dijkstra(origine: str, graph: Graph):

    waitGraph = dict(graph.graph)
    summits = {}
    path = {}
    summits[origine] = 0
    for summit in waitGraph:
        if summit != origine:
            summits[summit] = INF
    while waitGraph:
        minSummit = None
        for currSummit in waitGraph:
            if minSummit is None:
                minSummit = currSummit
            elif summits[minSummit] > summits[currSummit]:
                minSummit = currSummit
        for neighbour in graph.getNeigbours(minSummit):
            distance=summits[minSummit]+ graph.getWeight(minSummit,neighbour)
            if distance < summits[neighbour]:
                summits[neighbour] = distance
                path[neighbour] = minSummit
        waitGraph.pop(minSummit)

    return path




def rebuildShortestPath(graph:Graph,path:dict):
    ShortestPath = {}
    
    for summit in graph.graph:
        
        for item in path.items():
            
            if item[1]==summit:
                if  summit not in ShortestPath.keys():
                    ShortestPath.__setitem__(summit,list(item[0]))
                else:
                    ShortestPath[summit].append(list(item[0]))
                
    return ShortestPath


# def dijkstraHeap(origine: str, graph: Graph):
#     waitGraph = dict(graph.graph)
#     summits = {}
#     path = {}
#     summits[origine] = 0
#     for summit in waitGraph:
#         if summit != origine:
#             summits[summit] = INF
    
#     heap = Heap(graph.summitNumber)
#     parsedHeap = heap.parseDictToHeap(summits)
#     print(parsedHeap)



# dijkstraHeap("s",TestGraph)

# def extractMin(dict:dict):
#     return dict.popitem(0)[0]
# def cutSummit(dict:dict,v,dv):
#     heapObject = Heap(len(dict.keys()))
#     heapList = heapObject.parseDictToHeap(dict)
#     for value in heapList:
#         keys = getKeyFormValue(dict,value)
        
#         dict[keys.pop(0)]
        
#         # if value >=0:
#         #     keys = getKeyFormValue(dict,value)
#         #     tmp  =dict.__getitem__()
#         #     dict.__setitem__(keys[0],value)


# def getKeyFormValue(dict:dict,value):
#     keys = {i for i in dict if dict[i]==value}
#     return list(keys)
    




# # def extraireMin(queue:list,summits:dict):

# #     if queue != []:
# #         values=list(summits.values())

# #         sorted(values)
# #         print("values :",values)
# #         key=""
# #         for summit in summits:
# #             if values[0] == summits[summit]:
# #                 key = str(summit)
# #         indexA = queue.index(key)
# #         exchange(queue,0,indexA)

# #     else:
# #         print("queue is empty!!")
# #     return queue

# # def exchange(list,indexA,indexB):
# #     list[indexA], list[indexB] = list[indexB], list[indexA]

# # def heapify(summits:dict,adj):

# #     min =INF
# #     minItem=None
# #     listOfItems=list(summits.items())
# #     print(listOfItems)
# #     for item in listOfItems:
# #         if min >item[1]:

# #             minItem = item
# #             min=item[1]
# #     print('min :',min)
# #     adjIndex= listOfItems.index((adj,summits[adj]))

# #     index =listOfItems.index(minItem)
# #     listOfItems[adjIndex],listOfItems[index]=listOfItems[index],listOfItems[adjIndex]
# #     summits=dict(listOfItems)
# #     return summits


# ############### TEST##################
print(dijkstraQueue("s",TestGraph))

print(rebuildShortestPath( TestGraph,dijkstraQueue("s", TestGraph)))

RandomGraph = Graph()
RandomGraph = RandomGraph.generateRandomGraph(3,1)
print(RandomGraph) 