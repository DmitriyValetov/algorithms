

def merge(arr1, arr2):
    new_arr = []
    for _ in range(len(arr1) + len(arr2)):
        if len(arr1)==0 and len(arr2)>0:
            new_arr += arr2
            break
        elif len(arr1)>0 and len(arr2)==0:
            new_arr += arr1
            break
        elif arr1[0] < arr2[0]:
            new_arr.append(arr1.pop(0))
        else:
            new_arr.append(arr2.pop(0))
    return new_arr


def merge_sort(arr):
    """ sort from little to bigger """
    if len(arr) == 1:
        return arr

    first_half = arr[:len(arr)//2]
    second_half = arr[len(arr)//2:]
    return merge(merge_sort(first_half), merge_sort(second_half))


def get_unique_n(arr):
    sorted_numbers = merge_sort(arr)
    unique_n = 0
    current_value = None
    for v in sorted_numbers:
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


def main_mergesort():
    with open(file="input.txt", mode='r') as f:
        lines = f.readlines()

    numbers = list(map(int, lines[1].split()))
    sorted_numbers = merge_sort(numbers)
    
    with open(file="output.txt", mode='w') as f:
        f.write(" ".join(map(str, sorted_numbers)))


if __name__ == "__main__":
    main_unique()
