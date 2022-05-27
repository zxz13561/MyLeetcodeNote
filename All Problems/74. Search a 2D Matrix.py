from datetime import datetime as dt


def search_matrix(matrix, target):
    l_out = 0
    r_out = len(matrix) - 1
    while l_out <= r_out:
        mid_out = l_out + (r_out - l_out) // 2
        if matrix[mid_out][0] == target:
            return True
        elif matrix[mid_out][0] < target:
            l_out = mid_out + 1
        else:
            r_out = mid_out - 1
    l_in = 0
    r_in = len(matrix[r_out]) - 1
    while l_in <= r_in:
        mid_in = l_in + (r_in - l_in) // 2
        if matrix[r_out][mid_in] == target:
            return True
        elif matrix[r_out][mid_in] < target:
            l_in = mid_in + 1
        else:
            r_in = mid_in - 1
    return False


if __name__ == '__main__':
    input_matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    input_target = 23
    print(search_matrix(input_matrix, input_target))
    """
    for time in range(100):
        start = dt.now()
        search_matrix(input_matrix, input_target)
        duration = dt.now() - start
        print(str(time + 1) + ' Try : ' + str(duration.microseconds / 10000) + ' ms')
    """
