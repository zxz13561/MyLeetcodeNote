def move_zeroes(nums):
    j = 0
    for num in nums:
        if num != 0:
            nums[j] = num
            j += 1

    for x in range(j, len(nums)):
        nums[x] = 0


if __name__ == '__main__':
    input_nums = [0, 0, 1]
    print(move_zeroes(input_nums))
    print(input_nums)
