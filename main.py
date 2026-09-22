import time
from lessons.lesson4_2 import Remanga


def mtime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        print(f"Function {func.__name__} took {end_time - start_time} секунд")

        return result

    return wrapper


@mtime
def comsum(n):
    total = sum(range(n))
    return total


print(comsum(10000000))