

def merge(arr1, arr2):
    new_arr = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(arr1), len(arr2)
    for _ in range(left_list_length + right_list_length):
        if left_list_index==left_list_length and right_list_index<right_list_length:
            for i in range(right_list_index, right_list_length):
                new_arr.append(arr2[i])
            break
        elif left_list_index<left_list_length and right_list_index==right_list_length:
            for i in range(left_list_index, left_list_length):
                new_arr.append(arr1[i])
            break
        elif arr1[left_list_index] < arr2[right_list_index]:
            new_arr.append(arr1[left_list_index])
            left_list_index+=1
        else:
            new_arr.append(arr2[right_list_index])
            right_list_index+=1
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
