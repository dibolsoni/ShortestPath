from unittest import TestCase, main
from ShortestPath import \
    ShortestPath, NODES, CONNECTIONS


# inpired in Dijkstra Algorithm
class TestAShortestPath(TestCase):
    def setUp(self):
        self.sp = ShortestPath(NODES, CONNECTIONS)

    def test_available_connections_in_a_node(self):
        node = 'a'
        expected = [['a', 'b', 2], ['a', 'd', 8]]
        self.assertEqual(self.sp.available_connections(node), expected)
        node = 'b'
        expected = [['a', 'b', 2], ['b', 'd', 5], ['b', 'e', 6]]
        self.assertEqual(self.sp.available_connections(node), expected)


if __name__ == "__main__":
    main(verbosity=2)
