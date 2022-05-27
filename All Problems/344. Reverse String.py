from datetime import datetime as dt


def reverse_string(s):
    s.reverse()


if __name__ == '__main__':
    input_s = ["h", "e", "l", "l", "o"]
    print(reverse_string(input_s))
    print(input_s)
    """
    for time in range(100):
        start = dt.now()
        search_matrix(input_matrix, input_target)
        duration = dt.now() - start
        print(str(time + 1) + ' Try : ' + str(duration.microseconds / 10000) + ' ms')
    """
