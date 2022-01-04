NODES = ['a', 'b', 'c', 'd', 'e', 'f']
CONNECTIONS = [
    ['a', 'a', 0],
    ['a', 'b', 2],
    ['a', 'd', 8],
    ['b', 'd', 5],
    ['b', 'e', 6],
    ['d', 'e', 3],
    ['d', 'f', 2],
    ['f', 'e', 1],
    ['f', 'c', 3],
    ['c', 'e', 9]
]


# inspired in Dijkstra Algorithm
class ShortestPath:
    def __init__(self, nodes, connections):
        self.nodes = nodes
        self.connections = connections

    def available_connections(self, x):
        return [c for c in self.connections if x in c]

    def find_connection(self, x, y):
        c_list = [c for c in self.connections if x in c and y in c]
        return c_list[0] if c_list else None

    def distance(self, x, y):
        found = self.find_connection(x, y)
        return found[2] if found is not None else None

    def way(self, x, y):
        pass
