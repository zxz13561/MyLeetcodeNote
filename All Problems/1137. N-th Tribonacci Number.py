from datetime import datetime as dt


def nth(n):
    tri_list = [0, 1, 1]
    if n in tri_list:
        return tri_list[n]
    for val in range(3, n + 1):
        tri_list.append(tri_list[val - 1] + tri_list[val - 2] + tri_list[val - 3])
    return tri_list[-1]


if __name__ == '__main__':
    input_n = 0
    print(nth(input_n))
    """
    for time in range(100):
        start = dt.now()
        search_matrix(input_matrix, input_target)
        duration = dt.now() - start
        print(str(time + 1) + ' Try : ' + str(duration.microseconds / 10000) + ' ms')
    """
