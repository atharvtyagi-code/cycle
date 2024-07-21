class Graph():
    def __init__(self, vertices):
        self.graph = {}
        self.V = vertices

        for i in range(vertices):
            self.graph[i] = []

    def create_vertex(self, u, v):
        self.graph[u].append(v)

    def isCycle(self, V, visited, recursion_stack):
        visited[V] = True
        recursion_stack[V] = True
        for neighbor in self.graph[V]:
            if not visited[neighbor]:
                if self.isCycle(neighbor, visited, recursion_stack):
                    return True
                
            elif recursion_stack[neighbor]:
                return True
            
        recursion_stack[V] = False
        return False

    def check_cycle(self):
        visited = [False]*self.V
        recursion_stack = [False]*self.V

        for node in range(self.V):
            if not visited[node]:
                if self.isCycle(node, visited, recursion_stack):
                    return True
                
        return False


g = Graph(5)

g.create_vertex(0, 1)
g.create_vertex(0, 2)
g.create_vertex(1, 2)
g.create_vertex(1, 3)
g.create_vertex(2, 1)
#g.create_vertex(2, 3)
#g.create_vertex(3, 4)
g.create_vertex(3, 4)
g.create_vertex(4, 5)
#g.create_vertex(4, 5)

print(g.graph)
g1 = Graph(4)
g1.create_vertex(0, 1)
g1.create_vertex(0, 2)
g1.create_vertex(1, 2)
#g1.create_vertex(2, 0)
#g1.create_vertex(2, 3)
#g1.create_vertex(3, 3)

if g1.check_cycle():
    print("It is a cycle.")

else:
    print("It is not a cycle.")