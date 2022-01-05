from ShortestPath import ShortestPath

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

if __name__ == "__main__":
    sp = ShortestPath(NODES, CONNECTIONS)
    sp.shortest('a', 'e')
    sp.shortest('d', 'a')
