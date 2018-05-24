# Quang Lam

from xml.dom import minidom
import heapq
import operator
class VT:
    # Vertex/Cost Tuple
    def __init__(self, vertex, cost):
        self.vertex = vertex
        self.cost = cost
    def __repr__(self):
        return("VT(" + str(self.vertex.label) + ", " + str(self.cost) + ")")
    def __lt__(self,other):
        if type(self) != type(other):
            raise Exception("Unordered")
        return float(self.cost) < float(other.cost)

class Vertex:
    def __init__(self, vertexId, label, cost=0):
        self.vertexId = vertexId
        self.label = label
        self.cost = cost
        self.edges = []
        self.previous = None
    def addEdge(self,e):
        self.edges.append(e)
    def getEdges(self):
       return self.edges
    def __str__(self):
        res = "Vertex:\n    Label: " + str(self.label) + "\n    Cost: %1.2f"%self.cost
        if self.previous != None:
            res += "\n    Previous: " + str(self.previous.label)
        return res
    def __lt__(self,other):
        if type(self) != type(other):
            raise Exception("Unordered")
        return float(self.cost) < float(other.cost)

class Edge:
    def __init__(self, v1, v2, weight=0):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight
    def getEndpoints(self):
        return (self.v1, self.v2)

def dijkstra(vertexDict, edgeList, source):
    visited = set()
    unvisted = []

    source.cost = 0
    heapq.heappush(unvisted, VT(source, 0))

    while len(unvisted) > 0:
        current = heapq.heappop(unvisted)
        visited.add(current)
        for edge in current.vertex.getEdges():
            v = vertexDict[edge.v2]
            if edge.v2 == current.vertex.vertexId:
                v = vertexDict[edge.v1]
            if v not in visited:
                if v.cost > current.cost + edge.weight:
                    v.cost = current.cost + edge.weight
                    v.previous = current.vertex
                    heapq.heappush(unvisted, VT(v, current.cost + edge.weight))

def main():
    xmldoc = minidom.parse("graph.xml")

    graph = xmldoc.getElementsByTagName("Graph")[0]
    vertices = graph.getElementsByTagName("Vertices")[0].getElementsByTagName("Vertex")
    edges = graph.getElementsByTagName("Edges")[0].getElementsByTagName("Edge")

    vertexDict = {}

    source = None
    for vertex in vertices:
        vertexId = int(vertex.attributes["vertexId"].value)
        label = vertex.attributes["label"].value
        v = Vertex(vertexId, label, float("inf"))
        vertexDict[vertexId] = v
        if label == "0":
            source = v

    edgeList = []

    for edge in edges:
        head = int(edge.attributes["head"].value)
        tail = int(edge.attributes["tail"].value)
        anEdge = Edge(head, tail)
        if "weight" in edge.attributes:
            anEdge.weight = float(edge.attributes["weight"].value)
        edgeList.append(anEdge)
        vertexDict[head].addEdge(anEdge)
        vertexDict[tail].addEdge(anEdge)

    dijkstra(vertexDict, edgeList, source)

    for item in sorted(vertexDict.items(), key=operator.itemgetter(1)):
        print(item[1])

if __name__ == "__main__":
    main()