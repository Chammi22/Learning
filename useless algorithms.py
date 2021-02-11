import random


def generate_random_string(length):
    result = []
    for i in range(length):
        result.append(chr(random.randint(33, 126)))
    string = ''.join(result)
    return string


print(generate_random_string(10))
