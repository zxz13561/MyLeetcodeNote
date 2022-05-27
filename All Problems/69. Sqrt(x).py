

def my_sqrt(x: int) -> int:
    l = 1
    r = x
    while l <= r:
        m = (l + r) // 2
        m2 = m * m
        if m2 == x:
            return m
        if m2 > x:
            r = m - 1
        else:
            l = m + 1
    return l - 1


if __name__ == '__main__':
    print(my_sqrt(18496))
