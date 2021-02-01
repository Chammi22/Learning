from collections import Counter


def turn_over(number):
    result = 0
    while number != 0:
        result = result * 10 + number % 10
        number = number // 10
    return result


# print(turn_over(123))


def find_missing_number(list_of_number):
    length = len(list_of_number)
    for i in range(1, length + 1):
        if i in list_of_number:
            continue
        else:
            return i


# print(find_missing_number([1, 4, 6, 8, 7, 2, 3]))


def count_of_number(string):
    string = list(string)
    print(string)
    result = {}
    count = 0
    for element in set(string):
        for j in string:
            if j == element:
                count += 1
        if element not in result:
            result[element] = count
        while count != 0:
            string.remove(element)
            count -= 1
    print(string)
    return result


print(count_of_number('aaaabbbbbcccccddddd'))
print(Counter("aaaabbbbbcccccddddd"))
