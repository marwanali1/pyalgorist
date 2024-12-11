from collections import deque
from src.data_structures.graph import Graph, Vertex


def breadth_first_search(graph: Graph, search_value: Vertex.value) -> bool:
    """
    Time complexity: O(V + E) where V is the number of vertices in the graph and E is the number of
    edges
    """
    if graph.is_empty():
        return False

    def _breadth_first_search(vertex) -> None:
        visited = {}
        visited[vertex] = True

        queue = deque()
        queue.append(vertex)

        while queue:
            curr_vert = queue.popleft()
            if curr_vert.value == search_value:
                return True

            for adj_vert in curr_vert.adjacent_vertices:
                if adj_vert not in visited:
                    queue.append(adj_vert)
                    visited[adj_vert] = True

        return False

    return _breadth_first_search(graph.vertices[0])
