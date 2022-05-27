def min_sub_array_len(target, nums):
    limit = len(nums) + 1
    left = 0
    right = limit
    for index in range(len(nums)):
        target -= nums[index]
        while target <= 0:
            right = min(right, index - left + 1)
            target += nums[left]
            left += 1
    return right % limit


def min_sub_array_len_1(s, nums):
    total = 0
    left = 0
    right = 0
    result = len(nums) + 1
    while right < len(nums):
        total += nums[right]
        while total >= s:
            result = min(result, right - left + 1)
            total -= nums[left]
            left += 1
        right += 1
    return result if result <= len(nums) else 0


if __name__ == '__main__':
    input_target = 11
    # input_nums = [2, 3, 1, 2, 4, 3]
    # input_nums = [1, 1, 1, 1, 4, 1, 4]
    input_nums = [1, 2, 3, 4, 5]
    print(min_sub_array_len(input_target, input_nums))
