
def is_perfect_square(num) -> bool:
    left = 0
    right = num
    while left <= right:
        mid = left + (right - left) // 2
        sqrt = mid * mid
        if sqrt == num:
            return True
        elif sqrt > num:
            right = mid - 1
        else:
            left = mid + 1
    return False


if __name__ == '__main__':
    input_num = 17
    print(is_perfect_square(input_num))