import random
from mergesort3 import merge_sort, get_unique_n


def test_mergesort():
    cycles = 10
    N = 100
    for _ in range(cycles):
        unordered = [random.randint(0, 100) for _ in range(N)]
        sorted_by_mergesort = merge_sort(unordered)
        sorted_etalon = sorted(unordered) 
        assert(sorted_by_mergesort == sorted_etalon)

def test_unique_n():
    cycles = 10
    N = 100
    for _ in range(cycles):
        unordered = [random.randint(0, 100) for _ in range(N)]
        assert(get_unique_n(unordered) == len(set(unordered)))