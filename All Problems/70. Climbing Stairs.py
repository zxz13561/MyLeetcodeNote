from datetime import datetime as dt


def climb_stairs(n):
    if n < 2:
        return n
    s1, s2 = 1, 2
    for stair in range(n - 2):
        s1, s2 = s2, s1 + s2
    return s2


if __name__ == '__main__':
    input_n = 5
    print(climb_stairs(input_n))
    """
    for time in range(100):
        start = dt.now()
        search_matrix(input_matrix, input_target)
        duration = dt.now() - start
        print(str(time + 1) + ' Try : ' + str(duration.microseconds / 10000) + ' ms')
    """
