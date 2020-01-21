import random

from heap import Heap, slide_window_promo, split, slide_window_process_by_min_heap, slide_window_process_by_promo
from generate_inputs import insert_extracting_input, slide_window_mins

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
        

def test_list_split():
    for _ in range(100):
        N = random.randint(1, 100)
        K = random.randint(1, 100)
        if K > N:
            K = N
        arr = [i for i in range(N)]
        arrs = split(arr, K)
        assert(len(arrs)==N-K+1)

def test_list_split2():
    N = 100
    K = N
    arr = [i for i in range(N)]
    arrs = split(arr, K)
    assert(len(arrs)==N-K+1)
    assert(len(arrs)==1)
    assert(min(arr) == min(arrs[0]))


def test_sliding_promo():
    for _ in range(1):
        slide_window_mins(1, 150000, 1, 10000)
        slide_window_promo()

def test_slide_window_min_heap_vs_promo():
    for _ in range(10):
        slide_window_mins(1, 10000, 1, 10000)
        with open(file="input.txt", mode='r') as f:
            lines = f.readlines()
        heap_mins = slide_window_process_by_min_heap(lines)
        promo_mins = slide_window_process_by_promo(lines)
        assert(heap_mins == promo_mins)