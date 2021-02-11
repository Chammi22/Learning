def sieve(number):
    result = list(range(2, number + 1))
    for i in result:
        if i != 0:
            if i ** 2 < number:
                for n in range(i ** 2, number+1, i):
                    result[n-2] = 0
            
            else:
                break

    return [x for x in result if x != 0]


print(sieve(51))
