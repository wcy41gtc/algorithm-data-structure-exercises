## Dijkstra's Algorithm
# 1. Create a result dictionary. At the end of the program, result will have the shortest distance 
#    (value) for all nodes (key) in the graph. For our example, it will become as {'A': 0, 'B': 5, 'C': 3, 'D': 2, 'F': 6, 'E': 4}
# 2. Start with the source node. Distance from source to source itself is 0.  
# 3. The distance to all other nodes from the source is unknown initially, therefore set the initial distance to infinity.  
# 4. Create a set unvisited containing nodes that have not been visited. Initially, it will have all nodes of the graph.
# 5. Create a path dictionary that keeps track of the previous node (value) that can lead to the current node (key). 
#    At the end of the program, for our example, it will become as {'B': 'A', 'C': 'D', 'D': 'A', 'F': 'C', 'E': 'C'}. 
# 6. As long as unvisited is non-empty, repeat the following:
#    - Find the unvisited node having smallest known distance from the source node.  
#    - For the current node, find all the unvisited neighbours. For this, you have calculate the distance of each unvisited neighbour.  
#    - If the calculated distance of the unvisited neighbour is less than the already known distance in result dictionary, 
#      update the shortest distance in the result dictionary. 
#    - If there is an update in the result dictionary, you need to update the path dictionary as well for the same key. 
#    - Remove the current node from the unvisited set.

# Note - This implementation of the Dijkstra's algorithm is not very efficient. Currently it has a *O(n^2)* time complexity. 
# We will see a better version in the next lesson - "Graph Algorithms" with *O(nlogn)* time complexity.

from collections import defaultdict
import sys
class Graph:
    def __init__(self):
        self.nodes = set()                   # A set cannot contain duplicate nodes
        self.neighbours = defaultdict(list)  # Defaultdict is a child class of Dictionary that provides a default value for a key that does not exists.
        self.distances = {}                  # Dictionary. An example record as ('A', 'B'): 6 shows the distance between 'A' to 'B' is 6 units

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.neighbours[from_node].append(to_node)
        self.neighbours[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance    # lets make the graph undirected / bidirectional 
        
    def print_graph(self):
        print("Set of Nodes are: ", self.nodes)
        print("Neighbours are: ", self.neighbours)
        print("Distances are: ", self.distances)

import sys

'''Find the shortest path from the source node to every other node in the given graph'''
def dijkstra(graph, source):
    
    result = {}
    result[source] = 0                 
    
    for node in graph.nodes:
        if (node != source):
            result[node] = sys.maxsize
            
    unvisited = set(graph.nodes)  
    
    path = {}

    '''THE GREEDY APPROACH'''
    # As long as unvisited is non-empty
    while unvisited: 
        min_node = None    
        
        # 1. Find the unvisited node having smallest known distance from the source node.
        for node in unvisited:
            if node in result:
                
                if min_node is None:       
                    min_node = node
                elif result[node] < result[min_node]:
                    min_node = node

        if min_node is None:
            break
            
        # known distance of min_node
        current_distance = result[min_node]
        
        # 2. For the current node, find all the unvisited neighbours. 
        # For this, you have calculate the distance of each unvisited neighbour.
        for neighbour in graph.neighbours[min_node]:
            if neighbour in unvisited:
                distance = current_distance + graph.distances[(min_node, neighbour)]
            
                # 3. If the calculated distance of the unvisited neighbour is less than the already known distance in result dictionary, update the shortest distance in the result dictionary.
                if ((neighbour not in result) or (distance < result[neighbour])):
                    result[neighbour] = distance

                    # 4. If there is an update in the result dictionary, you need to update the path dictionary as well for the same key.
                    path[neighbour] = min_node
        
        # 5. Remove the current node from the unvisited set.
        unvisited.remove(min_node)

    return result

def test():
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_node("E")
    graph.add_node("F")
    
    graph.add_edge("A", "B", 5)
    graph.add_edge("A", "D", 9)
    graph.add_edge("A", "E", 2)
    graph.add_edge("B", "C", 2)
    graph.add_edge("C", "D", 3)
    graph.add_edge("D", "F", 2)
    graph.add_edge("E", "F", 3)
    
    result = dijkstra(graph, "A")
    print(result)

if __name__ == "__main__":
    test()