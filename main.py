from ShortestPath import ShortestPath, Connection

NODES = ['a', 'b', 'c', 'd', 'e', 'f']
CONNECTIONS = [
    Connection(['a', 'a'], 0),
    Connection(['a', 'b'], 2),
    Connection(['a', 'd'], 8),
    Connection(['b', 'd'], 5),
    Connection(['b', 'e'], 6),
    Connection(['d', 'e'], 3),
    Connection(['d', 'f'], 2),
    Connection(['f', 'e'], 1),
    Connection(['f', 'c'], 3),
    Connection(['c', 'e'], 9),
]

if __name__ == "__main__":
    sp = ShortestPath(CONNECTIONS)
    print('#1# level route')
    sp.shortest('d', 'a')
    sp.shortest('f', 'c')

    print('#2# level route')
    sp.shortest('a', 'e')
    sp.shortest('b', 'f')

    # sp.shortest('a', 'c')
