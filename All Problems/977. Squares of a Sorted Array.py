
def sorted_squares(nums):
    return sorted([x ** 2 for x in nums])


if __name__ == '__main__':
    input_nums = [0, 5, 3, 4, 4]

    print(sorted_squares(input_nums))
