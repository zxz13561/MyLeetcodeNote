
def is_bad_version(version) -> bool:
    bad = 4
    if version >= bad:
        return True
    else:
        return False


def first_bad_version(n):
    l_limit = 1
    r_limit = n

    while l_limit <= r_limit:
        mid = l_limit + (r_limit - l_limit) // 2
        if is_bad_version(mid):
            r_limit = mid - 1
        else:
            l_limit = mid + 1
    return l_limit


if __name__ == '__main__':
    i_n = 200
    print(first_bad_version(i_n))
