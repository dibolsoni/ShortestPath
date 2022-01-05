from functools import reduce


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

    def distance_way(self, way: list):
        return reduce(lambda a, w: a['dist'] + w['dist'], way)

    def ways(self, node_from: str, node_to: str) -> list:
        result = []
        for connection in self.available_connections(node_from):
            other = other_node(connection, node_from)
            for other_connection in self.available_connections(other):
                if node_to in other_connection['nodes']:
                    result.append([connection, other_connection])
        return result

    def shortest_way(self, way: list) -> list:
        if len(way) == 0:
            raise ValueError('must have 1 way at least')
        if len(way) == 1:
            return way
        return reduce(
            lambda a, w:
            a if self.distance_way(a) < self.distance_way(w)
            else w, way)

    def print_way(self, node_from, node_to, way: list):
        print('#'*20)
        print(f'trip from:{node_from} to:{node_to}')
        for i, c in enumerate(way):
            print(f'\t{i}- node:{c["nodes"][0]} to:{c["nodes"][1]}')
        print(f'total size:{self.distance_way(way)}')
        print('#'*20 + '\n')

    def shortest(self, node_from: str, node_to: str) -> None:
        ways = self.ways(node_from, node_to)
        way = self.shortest_way(ways)
        self.print_way(node_from, node_to, way)
