
def arrange_coins(n):
    l_limit = 0
    r_limit = 65536
    while l_limit <= r_limit:
        mid = l_limit + (r_limit - l_limit) // 2
        temp_result = mid * (mid + 1) / 2
        if temp_result == n:
            return mid
        elif temp_result > n:
            r_limit = mid - 1
        else:
            l_limit = mid + 1

    return l_limit - 1


def count_to_max():
    result = 0
    para = 0
    memory_max = (2 ** 31) - 1
    while result < memory_max:
        para += 1
        result = (para * (para + 1)) / 2
    return para


if __name__ == '__main__':
    i_n = 8
    print(arrange_coins(i_n))
