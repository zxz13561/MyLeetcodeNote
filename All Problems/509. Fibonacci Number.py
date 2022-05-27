import logging
from datetime import datetime as dt


def fib(n):
    table = {0: 0, 1: 1}
    if n <= 1:
        return n
    elif n == 2:
        return 1

    for i in range(2, n):
        table[i] = table[i - 1] + table[i - 2]

    return table[n - 1] + table[n - 2]


if __name__ == '__main__':
    input_n = 100000
    for time in range(10):
        start = dt.now()
        fib(input_n)
        duration = dt.now() - start
        print(str(time + 1) + ' Try : ' + str(duration.microseconds / 10000))

