def binary_algorithm(array, number):
    length = int(len(array))
    while array:
        if number < array[int(length / 2)]:
            array = array[0:int(length / 2)]
            length = int(length / 2)
            continue
        elif number > array[int(length / 2)]:
            array = array[int(length / 2):length]
            length = int(length / 2)
            continue
        elif number == array[int(length / 2)]:
            return array[int(length / 2)]
        else:
            return 0


# array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(binary_algorithm(array, 10))


def better_binary_algorithm(array, number):
    high = len(array) - 1
    low = 0

    while low <= high:
        middle = int((high + low) / 2)
        result = array[middle]
        if result == number:
            return middle
        elif number < result:
            high = middle - 1
        elif number > result:
            low = middle + 1
    return None


array = [1, 3, 4, 5, 6, 7, 8, 9]
print(better_binary_algorithm(array, 1))
