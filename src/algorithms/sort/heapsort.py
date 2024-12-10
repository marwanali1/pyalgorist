import heapq

from src.data_structures.heap import Heap


def heapsort(elems: list[int]) -> list[int]:
    heapq.heapify(elems)
    sorted_elems = []
    for _ in range(len(elems)):
        sorted_elems.append(heapq.heappop(elems))

    return sorted_elems


def max_heapsort(elems: list[int]) -> list[int]:
    heap = Heap()
    for elem in elems:
        heap.push(elem)

    sorted_elems = []
    for _ in range(len(elems)):
        sorted_elems.append(heap.pop())

    return sorted_elems
