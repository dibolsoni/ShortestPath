from functools import reduce
from dataclasses import dataclass

from typing import List

Node = str


@dataclass(frozen=True)
class Connection:
    nodes: List[Node]
    distance: int


Way = List[Connection]


# inspired in Dijkstra Algorithm
class ShortestPath:
    def __init__(self, connections: Way):
        self.connections = connections

    def available_connections(self, x: Node) -> Way:
        return [c for c in self.connections if x in c.nodes]

    def find_connection(self, x: Node, y: Node) -> Connection:
        if x == y:
            result = [c for c in self.connections if
                      x == c.nodes[0] and y == c.nodes[1]]
        else:
            result = [c for c in self.connections if
                      x in c.nodes and y in c.nodes]
        return result[0] if result else None

    @staticmethod
    def other_node(connection: Connection, node: Node) -> Node:
        return (connection.nodes[0]
                if connection.nodes[0] != node
                else connection.nodes[1])

    @staticmethod
    def nodes_in_connection(connection: Connection, x: Node, y: Node) -> bool:
        return x in connection.nodes and y in connection.nodes

    def distance(self, x, y) -> int:
        found = self.find_connection(x, y)
        return found.distance if found is not None else None

    @staticmethod
    def way_distance(way: Way):
        if len(way) == 1:
            return way[0].distance
        return reduce(lambda a, c: a.distance + c.distance, way)

    def ways(self, node_from: Node, node_to: Node) -> List[Way]:
        result = []
        root_connections = self.available_connections(node_from)
        for connection in root_connections:
            if self.nodes_in_connection(connection, node_from, node_to):
                result.append([connection])
                continue
            other = self.other_node(connection, node_from)
            for other_connection in self.available_connections(other):
                if node_from in connection.nodes \
                        and node_to in other_connection.nodes:
                    result.append([connection, other_connection])
        return result

    def shortest_way(self, ways: List[Way]) -> Way:
        if len(ways) == 0:
            raise ValueError('must have 1 ways at least')
        if len(ways) == 1:
            return ways
        return reduce(
            lambda a, w:
            a if self.way_distance(a) < self.way_distance(w)
            else w, ways)

    def print(self, node_from, node_to, way: Way) -> None:
        print('#' * 20)
        print(f'trip from:{node_from} to:{node_to}')
        for i, c in enumerate(way):
            print(f'\t{i}- node:{c.nodes[0]} to:{c.nodes[1]}')
        print(f'total size:{self.way_distance(way)}')
        print('#' * 20 + '\n')

    def shortest(self, node_from: Node, node_to: Node) -> Way:
        ways = self.ways(node_from, node_to)
        shortest = self.shortest_way(ways)
        self.print(node_from, node_to, shortest)
        return shortest
