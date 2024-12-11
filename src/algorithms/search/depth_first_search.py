from src.data_structures.graph import Graph, Vertex


def depth_first_search(graph: Graph, search_value: Vertex.value) -> bool:
    """
    Time complexity: O(V + E) where V is the number of vertices in the graph and E is the number of
    edges
    """
    if graph.is_empty():
        return False

    def _depth_first_search(vertex, visited: dict) -> bool:
        visited[vertex] = True

        if vertex.value == search_value:
            return True

        for adj_vert in vertex.adjacent_vertices:
            if adj_vert.value == search_value:
                return True

            if adj_vert not in visited:
                result = _depth_first_search(adj_vert, visited)

                if result:
                    return result

        return False

    return _depth_first_search(graph.vertices[0], {})
