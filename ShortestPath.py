NODES = ['a', 'b', 'c', 'd', 'e', 'f']
CONNECTIONS = [
    {'nodes': ['a', 'a'], 'dist': 0},
    {'nodes': ['a', 'b'], 'dist': 2},
    {'nodes': ['a', 'd'], 'dist': 8},
    {'nodes': ['b', 'd'], 'dist': 5},
    {'nodes': ['b', 'e'], 'dist': 6},
    {'nodes': ['d', 'e'], 'dist': 3},
    {'nodes': ['d', 'f'], 'dist': 2},
    {'nodes': ['f', 'e'], 'dist': 1},
    {'nodes': ['f', 'c'], 'dist': 3},
    {'nodes': ['c', 'e'], 'dist': 9}
]


def other_node(connection, node):
    for n in connection['nodes']:
        if n != node:
            return n


# inspired in Dijkstra Algorithm
class ShortestPath:
    def __init__(self, nodes, connections):
        self.nodes = nodes
        self.connections = connections

    def available_connections(self, x) -> list:
        return [c for c in self.connections if x in c['nodes']]

    def find_connection(self, x, y) -> dict:
        result = None
        if x == y:
            result = [c for c in self.connections if
                      x == c['nodes'][0] and y == c['nodes'][1]]
        else:
            result = [c for c in self.connections if
                      x in c['nodes'] and y in c['nodes']]
        return result[0] if result else None

    def distance(self, x, y) -> int:
        found = self.find_connection(x, y)
        return found['dist'] if found is not None else None

    def ways(self, x, y) -> list:
        result = []
        for connection in self.available_connections(x):
            other = other_node(connection, x)
            for other_connection in self.available_connections(other):
                if y in other_connection['nodes']:
                    result.append([connection, other_connection])
        return result
