from unittest import TestCase, main
from ShortestPath import \
    ShortestPath, NODES, CONNECTIONS


# inspired in Dijkstra Algorithm
class TestAShortestPath(TestCase):
    def setUp(self):
        self.sp = ShortestPath(NODES, CONNECTIONS)

    def test_available_connections_in_a_node(self):
        node = 'a'
        expected = [['a', 'a', 0], ['a', 'b', 2], ['a', 'd', 8]]
        self.assertEqual(self.sp.available_connections(node), expected)
        node = 'b'
        expected = [['a', 'b', 2], ['b', 'd', 5], ['b', 'e', 6]]
        self.assertEqual(self.sp.available_connections(node), expected)

    def test_distance_from_x_to_y(self):
        self.assertEqual(self.sp.distance('a', 'a'), 0)
        self.assertEqual(self.sp.distance('a', 'b'), 2)

    def test_distance_from_x_to_y_inverse(self):
        self.assertEqual(self.sp.distance('b', 'a'), 2)

    def test_distance_from_x_to_y_that_dont_connects(self):
        self.assertEqual(self.sp.distance('a', 'c'), None)

    def test_a_way_to_a_node(self):
        pass


if __name__ == "__main__":
    main(verbosity=2)
