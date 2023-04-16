import random
class Graph:

    """
    We chose to define our graphes with dictionnary to be performant enough
    """

    def __init__(self,graph={}):
        """Constructor"""
        self.ridgeNumber=0
        self.graph = graph
        self.summitNumber=len(self.graph.keys())
     

    def add_summit(self, summit):
        """
        To add a summit, we have to see if it already exists. If it does not, we can add it to our dictionary
        """
        if summit not in self.graph:
            self.graph[summit] = {}
            self.summitNumber += 1

    def add_ridge(self, summitA, summitB, weight):
        """
        To had a ridge, we have to check if the summits are in the graph, 
        and after we add the value of the ridge to the dictionnary

        """
        if summitA in self.graph and summitB in self.graph:
            if not(summitB in self.graph[summitA].keys()):
                self.graph[summitA].__setitem__(summitB,weight)
                self.ridgeNumber += 1

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
        return self.graph[summitA][summitB]
    
    def __str__(self) -> str:
        """Overides the print function"""
        res="Representation of our Graph \n"
        res += self.graph.__str__()

        return res
    
    def getSummits(self):
        """
        Returns a list of all graph summits"""
        return list(self.graph.keys())
    

    def getNeigbours(self,summit):
        """Returns a list of all neighbours of q given graph"""
        return list(self.graph[summit].keys())


    def generateRandomGraph(self,n,d):
        """Generate Random Graph from a given nuber of Summits and a density"""

        for i in range(n):
            self.add_summit(str(i))
        
            
        density = self.ridgeNumber/(2*self.summitNumber)
        
        while density != d:
            randomSummitA = random.randint(0,n)
            randomSummitB = random.randint(0,n)
            if randomSummitA != randomSummitB:
                self.add_ridge(str(randomSummitA),str(randomSummitB),random.randint(1,n))
               
            density = self.ridgeNumber/(2*self.summitNumber)
    
        return self









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
