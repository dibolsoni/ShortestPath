NODES = ['a', 'b', 'c', 'd', 'e', 'f']
CONNECTIONS = {
    ['a', 'b', 2],
    ['a', 'd', 8],
    ['b', 'd', 5],
    ['b', 'e', 6],
    ['d', 'e', 3],
    ['d', 'f', 2],
    ['f', 'e', 1],
    ['f', 'c', 3],
    ['c', 'e', 9]
}

class ShortestPath:
    def __init__(self, nodes, connections):
        self.nodes = nodes
        self.connections = connections

    def available_connections(self, x):
        return [c for c in self.connections if x in c]

    def distance(self, x, y):
        pass

    def way(self, x, y):
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
