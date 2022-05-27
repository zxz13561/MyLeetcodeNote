
def special_array(numbers):
    numbers.sort(reverse=True)
    num_len = len(numbers)

    l_x = 0
    r_x = num_len
    while l_x <= r_x:
        num_i = 0
        mid_x = l_x + (r_x - l_x) // 2

        l_index = 0
        r_index = num_len - 1
        while l_index <= r_index:
            mid_index = l_index + (r_index - l_index) // 2
            if mid_x == numbers[mid_index]:
                num_i = numbers.index(numbers[mid_index])
                break
            elif mid_x > numbers[mid_index]:
                l_index = mid_index + 1
            else:
                r_index = mid_index - 1
            num_i = l_index

        remain_num = num_len - num_i
        if remain_num == mid_x:
            return mid_x
        elif remain_num > mid_x:
            l_x = mid_x + 1
        else:
            r_x = mid_x - 1

    return -1


if __name__ == '__main__':
    input_nums = [0, 0, 3, 4, 4]

    print(special_array(input_nums))
