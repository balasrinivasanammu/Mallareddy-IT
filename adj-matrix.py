# Adjacency Matrix representation in Python
class Graph(object):
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        print(self.adjMatrix)

    def add_edge(self, v1, v2):        
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print(val,end=" ")
            print()
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.print_matrix()
