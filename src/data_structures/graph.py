from typing import TypeVar, Self

T = TypeVar("T")


class Vertex:
    def __init__(self, value: T) -> None:
        self._value = value
        self._adjacent_vertices = []

    @property
    def value(self) -> T:
        return self._value

    @property
    def adjacent_vertices(self) -> list[Self]:
        return self._adjacent_vertices

    def __repr__(self) -> str:
        return f"Vertex({self.value})"

    def __str__(self) -> str:
        return self.value

    def add_adjacent_vertex(self, vertex: Self) -> None:
        self.adjacent_vertices.append(vertex)
        vertex.adjacent_vertices.append(self)


class Graph:
    def __init__(self) -> None:
        self._vertices = []

    @property
    def vertices(self) -> list[Vertex]:
        return self._vertices

    def add_edge(self, first_vertex: Vertex, second_vertex: Vertex) -> None:
        self.vertices.append(first_vertex)
        self.vertices.append(second_vertex)
        first_vertex.add_adjacent_vertex(second_vertex)

    def is_empty(self) -> bool:
        return not self.vertices
