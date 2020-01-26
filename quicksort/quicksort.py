def partition(nums, low, high):  
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    pivot = nums[(low + high) // 2] # value to compare
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]

def quicksort(nums):  
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high: # otherwise happens at the ground of recursion
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high) # all movement is here
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


def get_unique_n(arr):
    quicksort(arr)
    unique_n = 0
    current_value = None
    for v in arr:
        if current_value != v:
            unique_n += 1
            current_value = v
    return unique_n


def main_unique():
    with open(file="input.txt", mode='r') as f:
        lines = f.readlines()

    numbers = list(map(int, lines[1].split()))
    unique_n = get_unique_n(numbers)
    
    with open(file="output.txt", mode='w') as f:
        f.write(str(unique_n))


def main_quicksort():
    with open(file="input.txt", mode='r') as f:
        lines = f.readlines()

    numbers = list(map(int, lines[1].split()))
    quicksort(numbers)
    
    with open(file="output.txt", mode='w') as f:
        f.write(" ".join(map(str, numbers)))


if __name__ == "__main__":
    main_quicksort()
    # main_unique()
