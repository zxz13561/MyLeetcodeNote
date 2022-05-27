
def two_sum(numbers, target):
    d = {}

    for i in range(len(numbers)):
        diff = target - numbers[i]
        if diff in d:
            return [d.get(diff) + 1, i + 1]
        else:
            d[numbers[i]] = i
    return


if __name__ == '__main__':
    input_nums = [2, 3, 4, 7, 11, 12]
    input_t = 9

    print(two_sum(input_nums, input_t))
