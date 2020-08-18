def ispolindrome(str):
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


str = "romamor"
print(ispolindrome(str))


def Polindrome(string):
    if string == string[::-1]:
        return True
    return False


print(Polindrome("abccba"))


def getdigit(number):
    Tup = [int(i) for i in str(number)]
    print(Tup)


number = 1233312
getdigit(number)


def get_longest_word(str):
    str = str.split()
    print(str)
    word_index = 0
    word_length = 0
    count = -1
    for i in str:
        count += 1
        if len(i) > word_length:
            word_length = len(i)
            word_index = count
    print(str[word_index])


get_longest_word("Python is simple and effective")


def get_pairs(List):
    result = list()
    for i in range(0, int(len(List)) - 1):
        result.append((List[i], List[i + 1]))
    print(result)


get_pairs(["What`s", "up", 'Roma', 'maybe', 'some', 'dota?'])
