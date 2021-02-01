def sum_of_element(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    else:
        return array[0] + sum_of_element(array[1:])


# print(sum_of_element([1, 2, 3, 4, 5]))


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        basis = array[0]
        less = [l for l in array[1:] if l <= basis]
        more = [m for m in array[1:] if m > basis]
        return quick_sort(less) + [basis] + quick_sort(more)


print(quick_sort([1, 5, 4, 7, 10]))
