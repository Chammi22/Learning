def is_polindrome(str):
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


str = "romamor"
print(is_polindrome(str))


def polindrome(string):
    if string == string[::-1]:
        return True
    return False


print(polindrome("abccba"))


def get_digit(number):
    tuple = [int(i) for i in str(number)]
    print(tuple)


number = 1233312
get_digit(number)


def length(element):
    return len(element)


def get_longest_word(string):
    string = string.split()
    string.sort(reverse=True, key=length)
    print(string[0])


def get_max_word(string):
    string = string.split()
    print(max(string, key=length))


#
#
get_longest_word("Python is simple and effective")


def get_pairs(List):
    result = list()
    for i in range(0, int(len(List)) - 1):
        result.append((List[i], List[i + 1]))
    print(result)


get_pairs(["What`s", "up", 'Roma', 'maybe', 'some', 'dota?'])
