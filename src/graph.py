import random

class Graph:
    def __init__(self, matrix):
        self.graph = matrix
        self.edges = []
        self.vertices = set()
        self.vertices_position = dict()

        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                if matrix[i][j] != 0:
                    self.edges.append((i, j, matrix[i][j]))
                    self.vertices.add(i)
                    self.vertices.add(j)
        
        # generate random position for vertices (x, y)
        for i in range(len(self.vertices)):
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            self.vertices_position[i] = (x, y)
        
        # sort edges by weight (ascending)
        self.edges.sort(key=lambda x: x[2])
    
    def add_edge(self, source, destination, weight):
        self.edges.append((source, destination, weight))

    def remove_edge(self, source, destination, weight):
        self.edges.remove((source, destination, weight))
    
    def add_vertex(self, vertex):
        self.vertices.add(vertex)

        x = random.randint(0, 100)
        y = random.randint(0, 100)
        self.vertices_position[vertex] = (x, y)

    def remove_vertex(self, vertex):
        self.vertices.remove(vertex)
        self.vertices_position.pop(vertex)
    
    def reset(self):
        self.edges = []
        self.vertices = set()
        self.vertices_position = dict()

        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                if matrix[i][j] != 0:
                    self.edges.append((i, j, matrix[i][j]))
                    self.vertices.add(i)
                    self.vertices.add(j)
        
        # generate random position for vertices (x, y)
        for i in range(len(vertices)):
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            self.vertices_position[i] = (x, y)
        
        # sort edges by weight (ascending)
        self.edges.sort(key=lambda x: x[2])

    def __cycle__(edge, edges):
        visited = set()
        queue = []
        queue.append(edge[0])

        while len(queue) > 0:
            current = queue.pop(0)
            visited.add(current)
            for edge in edges:
                if edge[0] == current and not edge[1] in visited:
                    queue.append(edge[1])
                elif edge[1] == current and not edge[0] in visited:
                    queue.append(edge[0])
        
        return edge[1] in visited
    
    def __kruskal_util__(self, edges):
        min = 1e9
        min_edge = None

        for edge in self.edges:
            if __cycle__(edge, edges):
                continue
            elif edge[2] < min:
                min = edge[2]
                min_edge = edge
        
        return min_edge
    
    def kruskal(self):
        self.reset()

        mst = []
        mst.push(self.edges[0])
        self.edges.pop(0)

        while len(mst) < len(self.vertices) - 1:
            edge = __kruskal_util__(self, mst)
            mst.append(edge)
            self.edges.remove(edge)
        
        self.edges = mst
    
    def __prim_util__(self, visited):
        min = 1e9
        min_edge = None

        for edge in self.edges:
            if edge[0] in visited and edge[1] in visited:
                continue
            elif edge[0] in visited or edge[1] in visited:
                if edge[2] < min:
                    min = edge[2]
                    min_edge = edge
        
        return min_edge
    
    def prim(self):
        self.reset()

        visited = set()
        mst = []
        mst.append(self.edges[0])
        visited.add(self.edges[0][0])
        visited.add(self.edges[0][1])
        self.edges.pop(0)

        while len(visited) < len(self.vertices):
            edge = __prim_util__(self, visited)
            mst.append(edge)
            visited.add(edge[0])
            visited.add(edge[1])
            self.edges.remove(edge)
        
        self.edges = mst
    
    def tree_weight(self):
        weight = 0
        for edge in self.edges:
            weight += edge[2]
        
        return weight
    
    def clustering(self, number):
        self.reset()
        clusters = []

if __name__ == "__main__":
    list = [[0, 4, 0, 0, 0, 0, 0], [4, 0, 1, 3, 0, 0, 0], [0, 1, 0, 2, 0, 0, 0], [0, 3, 2, 0, 1, 0, 0], [0, 0, 0, 1, 0, 2, 0], [0, 0, 0, 0, 2, 0, 3], [0, 0, 0, 0, 0, 3, 0]]
    graph = Graph(list)
    print(graph)