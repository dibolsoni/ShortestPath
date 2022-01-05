from unittest import TestCase, main
from ShortestPath import ShortestPath

from main import NODES, CONNECTIONS


# inspired in Dijkstra Algorithm
class TestAShortestPath(TestCase):
    def setUp(self):
        self.sp = ShortestPath(CONNECTIONS)

    def test_available_connections_in_a_node(self):
        node = 'a'
        expected = [{'dist': 0, 'nodes': ['a', 'a']},
                    {'dist': 2, 'nodes': ['a', 'b']},
                    {'dist': 8, 'nodes': ['a', 'd']}]
        self.assertEqual(expected, self.sp.available_connections(node))
        node = 'b'
        expected = [{'dist': 2, 'nodes': ['a', 'b']},
                    {'dist': 5, 'nodes': ['b', 'd']},
                    {'dist': 6, 'nodes': ['b', 'e']}]
        self.assertEqual(expected, self.sp.available_connections(node))

    def test_distance_from_x_to_y(self):
        self.assertEqual(self.sp.distance('a', 'a'), 0)
        self.assertEqual(self.sp.distance('a', 'b'), 2)

    def test_distance_from_x_to_y_inverse(self):
        self.assertEqual(self.sp.distance('b', 'a'), 2)

    def test_distance_from_x_to_y_that_dont_connects(self):
        self.assertEqual(self.sp.distance('a', 'c'), None)

    def test_a_way_to_a_node(self):
        expected = [[{'dist': 2, 'nodes': ['a', 'b']},
                     {'dist': 6, 'nodes': ['b', 'e']}],
                    [{'dist': 8, 'nodes': ['a', 'd']},
                     {'dist': 3, 'nodes': ['d', 'e']}]]
        self.assertEqual(expected, self.sp.ways('a', 'e'))
        expected = [[{'dist': 6, 'nodes': ['b', 'e']},
                     {'dist': 9, 'nodes': ['c', 'e']}]]
        self.assertEqual(expected, self.sp.ways('b', 'c'))

    def test_a_shortest_distance_in_ways(self):
        ways = [[{'dist': 2, 'nodes': ['a', 'b']},
                 {'dist': 6, 'nodes': ['b', 'e']}],
                [{'dist': 8, 'nodes': ['a', 'd']},
                 {'dist': 3, 'nodes': ['d', 'e']}]]
        expected = [{'dist': 2, 'nodes': ['a', 'b']},
                    {'dist': 6, 'nodes': ['b', 'e']}]
        self.assertEqual(expected, self.sp.shortest_way(ways))


if __name__ == "__main__":
    main(verbosity=2)
