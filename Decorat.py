def decorator_new(arg):
    def decorator(func):
        import time

        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"Time with arg {arg}  {end - start}")
            return result

        return wrapper
    return decorator


def turn_over(number):
    result = 0
    while number != 0:
        result = result * 10 + number % 10
        number = number // 10
    return result


print(decorator_new(33)(turn_over)(12345))



