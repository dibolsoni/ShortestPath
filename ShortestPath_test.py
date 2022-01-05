from unittest import TestCase, main
from ShortestPath import ShortestPath, Connection

from main import NODES, CONNECTIONS


# inspired in Dijkstra Algorithm
class TestAShortestPath(TestCase):
    def setUp(self):
        self.sp = ShortestPath(CONNECTIONS)

    def test_available_connections_in_a_node(self):
        node = 'a'
        expected = [Connection(['a', 'a'], 0),
                    Connection(['a', 'b'], 2),
                    Connection(['a', 'd'], 8)]
        self.assertEqual(expected, self.sp.available_connections(node))
        node = 'b'
        expected = [Connection(['a', 'b'], 2),
                    Connection(['b', 'd'], 5),
                    Connection(['b', 'e'], 6)]
        self.assertEqual(expected, self.sp.available_connections(node))

    def test_distance_from_x_to_y(self):
        self.assertEqual(self.sp.distance('a', 'a'), 0)
        self.assertEqual(self.sp.distance('a', 'b'), 2)

    def test_distance_from_x_to_y_inverse(self):
        self.assertEqual(self.sp.distance('b', 'a'), 2)

    def test_distance_from_x_to_y_that_dont_connects(self):
        self.assertEqual(self.sp.distance('a', 'c'), None)

    def test_a_way_to_a_node(self):
        expected = [[Connection(['a', 'b'], 2),
                     Connection(['b', 'e'], 6)],
                    [Connection(['a', 'd'], 8),
                     Connection(['d', 'e'], 3)]]
        self.assertEqual(expected, self.sp.ways('a', 'e'))
        expected = [[Connection(['b', 'e'], 6),
                     Connection(['c', 'e'], 9)]]
        self.assertEqual(expected, self.sp.ways('b', 'c'))

    def test_a_shortest_distance_in_ways(self):
        ways = [[Connection(['a', 'b'], 2),
                 Connection(['b', 'e'], 6)],
                [Connection(['a', 'd'], 8),
                 Connection(['d', 'e'], 3)]]
        expected = [Connection(['a', 'b'], 2),
                    Connection(['b', 'e'], 6)]
        self.assertEqual(expected, self.sp.shortest_way(ways))


if __name__ == "__main__":
    main(verbosity=2)
