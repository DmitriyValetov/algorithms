from heap_min import Heap
import random


def test_sort_insert():
    cycles = 10
    N = 100
    for _ in range(cycles):
        unordered = [random.randint(0, 100) for _ in range(N)]
        heap = Heap()
        heap.buildHeap(unordered.copy(), alg='insert')
        ordered = heap.ordered()
        assert(ordered == sorted(ordered.copy()))


def test_sort_siftUp():
    cycles = 10
    N = 1000
    for _ in range(cycles):
        unordered = [random.randint(0, 100) for _ in range(N)]
        heap = Heap()
        heap.buildHeap(unordered.copy(), alg='sift_up')
        ordered = heap.ordered()
        assert(ordered == sorted(ordered.copy()))


def test_sort_siftDown():
    cycles = 10
    N = 1000
    for _ in range(cycles):
        unordered = [random.randint(0, 100) for _ in range(N)]
        heap = Heap()
        heap.buildHeap(unordered.copy(), alg='sift_down')
        ordered = heap.ordered()
        assert(ordered == sorted(ordered.copy()))


