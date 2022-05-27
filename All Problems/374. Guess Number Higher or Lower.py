
def guess(num: int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    return 0


def guess_number(n: int) -> int:
    border_l = 1
    border_r = n

    while border_l <= border_r:
        guess_num = border_l + (border_r - border_l) // 2
        check_num = guess(guess_num)
        if check_num == -1:
            border_r = guess_num - 1
        elif check_num == 1:
            border_l = guess_num + 1
        else:
            return guess_num
    return -1


if __name__ == '__main__':
    global pick
    pick = 10

    print(guess_number(10))
