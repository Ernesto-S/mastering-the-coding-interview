# Edge list [[0,2], [2,3], [2,1], [1,3]]

# Adjacency list:
# {
#     0: [2],
#     1: [2, 3],
#     2: [3, 1],
#     3: [1, 2]
# }

# Adjacency matrix:
# [
#     [0, 0, 1, 0],
#     [0, 0, 1, 1],
#     [0, 1, 0, 1],
#     [0, 1, 1, 0]
# ]

class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []  # List of edges to other nodes
        self.visited = False

class Graph:
    def __init__(self):
        self.nodes = {}  # Dictionary to hold nodes by their value

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)

    def add_edge(self, from_value, to_value):
        if from_value in self.nodes and to_value in self.nodes:
            self.nodes[from_value].edges.append(self.nodes[to_value])
            self.nodes[to_value].edges.append(self.nodes[from_value])

    def get_node(self, value):
        return self.nodes.get(value)

    def __str__(self):
        return str({node.value: [edge.value for edge in node.edges] for node in self.nodes.values()})

# Example usage
graph = Graph()
graph.add_node(0)
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)
graph.add_node(6)


graph.add_edge(3, 1)
graph.add_edge(3, 4)
graph.add_edge(4, 2)
graph.add_edge(4, 5)
graph.add_edge(1, 2)
graph.add_edge(1, 0)
graph.add_edge(0, 2)
graph.add_edge(6, 5)
print(graph)  # Should print the adjacency list representation of the graph
