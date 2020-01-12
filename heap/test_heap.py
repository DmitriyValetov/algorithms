import random

from heap import Heap
from generate_inputs import insert_extracting_input

def test_sort_insert():
    cycles = 10
    N = 100
    for _ in range(cycles):
        unordered = [random.randint(0, 100) for _ in range(N)]
        heap = Heap(type=random.choice(['min', 'max']))
        heap.buildHeap(unordered.copy(), alg='insert')
        ordered = heap.ordered()
        assert(ordered == sorted(ordered.copy()))


def test_sort_siftUp():
    cycles = 10
    N = 1000
    for _ in range(cycles):
        unordered = [random.randint(0, 100) for _ in range(N)]
        heap = Heap(type=random.choice(['min', 'max']))
        heap.buildHeap(unordered.copy(), alg='sift_up')
        ordered = heap.ordered()
        assert(ordered == sorted(ordered.copy()))


def test_sort_siftDown():
    N = 100
    for _ in range(100):
        unordered = [random.randint(0, 50) for _ in range(N)]
        heap = Heap(type=random.choice(['min', 'max']))
        # heap = Heap(type='max')
        heap.buildHeap(unordered.copy(), alg='sift_down')
        ordered = heap.ordered()
        assert(ordered == sorted(ordered.copy()))


def test_insert_extract():
    for _ in range(100):
        insert_extracting_input(n_max=100, N=50)
        with open(file="input.txt", mode='r') as f:
            lines = f.readlines()

        numbers = []
        heap = Heap(type='max')
        for line in lines[1:]:
            if line[0] == '0':
                new_number = int(line.split()[1])
                numbers.append(new_number)
                numbers.sort(reverse=True)
                heap.add(new_number)
                assert(heap.list[0] == numbers[0])
            
            elif line[0] == '1':
                extracted = heap.pop()
                assert(extracted == numbers.pop(0))
        