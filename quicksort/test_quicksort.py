import random
from quicksort import quicksort, get_unique_n


def test_mergesort():
    cycles = 10
    N = 100
    for _ in range(cycles):
        numbers = [random.randint(0, 100) for _ in range(N)]
        sorted_etalon = sorted(numbers.copy()) 
        quicksort(numbers)
        assert(numbers == sorted_etalon)

def test_unique_n():
    cycles = 10
    N = 100
    for _ in range(cycles):
        unordered = [random.randint(0, 100) for _ in range(N)]
        assert(get_unique_n(unordered) == len(set(unordered)))