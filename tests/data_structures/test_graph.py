import unittest
from src.data_structures.graph import Graph, Vertex
from src.algorithms.search.depth_first_search import depth_first_search
from src.algorithms.search.bredth_first_search import breadth_first_search


class TestTrie(unittest.TestCase):
    TEST_GRAPH = None

    @classmethod
    def setUpClass(cls) -> None:
        alice = Vertex("alice")
        bob = Vertex("bob")
        candy = Vertex("candy")
        derek = Vertex("derek")
        elaine = Vertex("elaine")
        fred = Vertex("fred")
        helen = Vertex("helen")
        gina = Vertex("gina")
        irena = Vertex("irena")

        social_graph = Graph()

        social_graph.add_edge(alice, bob)
        social_graph.add_edge(alice, candy)
        social_graph.add_edge(alice, derek)
        social_graph.add_edge(alice, elaine)
        social_graph.add_edge(bob, fred)
        social_graph.add_edge(fred, helen)
        social_graph.add_edge(helen, candy)
        social_graph.add_edge(derek, gina)
        social_graph.add_edge(derek, elaine)
        social_graph.add_edge(gina, irena)

        cls.TEST_GRAPH = social_graph

    def test_contains_vertex_dfs(self) -> None:
        search_result = depth_first_search(self.TEST_GRAPH, "gina")
        self.assertTrue(search_result)

    def test_does_not_contain_vertex_dfs(self) -> None:
        self.assertFalse(depth_first_search(self.TEST_GRAPH, "john"))

    def test_contains_vertex_bfs(self) -> None:
        self.assertTrue(breadth_first_search(self.TEST_GRAPH, "alice"))

    def test_does_not_contain_vertex_bfs(self) -> None:
        self.assertFalse(breadth_first_search(self.TEST_GRAPH, "isaac"))


if __name__ == "__main__":
    unittest.main()
