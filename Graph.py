class Graph:

    """
    We chose to define our graphes with dictionnary to be performant enough
    """

    def __init__(self):
        """Constructor"""
        self.size =0
        self.graph = {}
     

    def add_summit(self, summit):
        """
        To add a summit, we have to see if it already exists. If it does not, we can add it to our dictionary
        """
        if summit not in self.graph:
            self.graph[summit] = {}
            self.size += 1

    def add_ridge(self, summitA, summitB, weight):
        """
        To had a ridge, we have to check if the summits are in the graph, 
        and after we add the value of the ridge to the dictionnary

        """
        if summitA in self.graph and summitB in self.graph:
            if not(summitB in self.graph[summitA].keys()):
                self.graph[summitA].__setitem__(summitB,weight)

    def cancel_summit(self, summit):
        """
        To cancel a ridge, we have to cancel the summit
        """
        if summit in self.graph:
            del self.graph[summit]
            for otherSummit in self.graph:
                del self.graph[otherSummit][summit]

    def cancel_ridge(self, summitA, summitB):
        """
        To cancel a ridge, we have to check that summits are in the graph AND after cancel the ridge
        """
        if summitA in self.graph and summitB in self.graph[summitB]:
            del self.graph[summitA][summitB]

    def isConected(self, summitA, summitB):
        """
        We research if there is a ridge between the summitA and summitB
        """
        if summitA in self.graph and summitB in self.graph[summitA]:
            return True
        return False
    def getWeight(self,summitA,summitB):
        return self.graph[summitA]
    def __str__(self) -> str:
        """Overides the print function"""
        res="Representation of our Graph \n"
        res += self.graph.__str__()
        # for summit in self.graph:
        #     child =self.graph[summit]
            
            # if child != {}:
            #     res += summit +" is connected to "+child[0]+" with the weight "+child[1] +"\n"
            # else:
            #     res += summit
        return res
    def getSummits(self):
        return self.graph.keys()
        

        


############### TEST##################
# graph = Graph()
# graph.add_summit("A")
# graph.add_summit("B")
# graph.add_summit("C")
# graph.add_summit("D")
# graph.add_ridge("A","B",7)
# graph.add_ridge("A","C",9)
# graph.add_ridge("B","D",10)
# graph.add_ridge("C","D",1 )
# print(graph)
