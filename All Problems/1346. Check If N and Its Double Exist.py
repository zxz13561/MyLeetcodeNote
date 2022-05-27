from datetime import datetime as dt


def check_if_exist(arr):
    for val in arr:
        if val != 0 and val % 2 == 0:
            try:
                arr.index(val / 2)
                return True
            except ValueError:
                continue
        elif val == 0:
            arr.remove(0)
            try:
                arr.index(0)
                return True
            except ValueError:
                continue
    return False


def binary_search(self, target, arr):
    l_limit = 0
    r_limit = len(arr) - 1
    while l_limit <= r_limit:
        mid = l_limit + (r_limit - l_limit) // 2
        if target == arr[mid]:
            return True
        elif target > arr[mid]:
            l_limit = mid + 1
        else:
            r_limit = mid - 1
    return False


def check_if_exist_binary_search(self, arr):
    if arr.count(0) > 1:
        return True
    for val in arr:
        if val != 0 and val % 2 == 0:
            try:
                arr.index(val / 2)
                return True
            except ValueError:
                continue
    return False


if __name__ == '__main__':
    input_arr = [3, 4, 5, 6]
    print(check_if_exist_new(input_arr))
    """
    for time in range(100):
        start = dt.now()
        search_matrix(input_matrix, input_target)
        duration = dt.now() - start
        print(str(time + 1) + ' Try : ' + str(duration.microseconds / 10000) + ' ms')
    """
