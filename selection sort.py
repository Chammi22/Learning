def find_largest_elemet(array):
    max = array[0]
    max_index = 0
    for index in range(1, len(array)):
        if max < array[index]:
            max = array[index]
            max_index = index
    return max_index


def selection_sort(array):
    result = []
    for i in range(len(array)):
        result.append(array.pop(find_largest_elemet(array)))
    return result


print(selection_sort([1, 4, 6, 8, 3, 2, 7, 9, 9, 10]))
