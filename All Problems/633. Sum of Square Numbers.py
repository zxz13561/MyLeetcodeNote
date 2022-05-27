from datetime import datetime as dt


def judge_square_sum(c):
    l_limit = 0
    r_limit = int(c ** 0.5)
    while l_limit <= r_limit:
        curr = l_limit * l_limit + r_limit * r_limit
        if curr < c:
            l_limit += 1
        elif curr > c:
            r_limit -= 1
        else:
            return True
    return False


if __name__ == '__main__':
    input_c = 10
    print(judge_square_sum(input_c))
    """
    for time in range(100):
        start = dt.now()
        search_matrix(input_matrix, input_target)
        duration = dt.now() - start
        print(str(time + 1) + ' Try : ' + str(duration.microseconds / 10000) + ' ms')
    """
