def merge(left_list, right_list):  
    sorted_list = []
    left_list_index = right_list_index = 0

    # Длина списков часто используется, поэтому создадим переменные для удобства
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если достигнут конец правого списка, элементы левого списка
        # добавляем в отсортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):  
    # Возвращаем список, если он состоит из одного элемента
    if len(nums) <= 1:
        return nums

    # Для того чтобы найти середину списка, используем деление без остатка
    # Индексы должны быть integer
    mid = len(nums) // 2

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)


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
