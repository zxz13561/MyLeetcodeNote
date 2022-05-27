def triangle_number(nums):
    nums, count, n = sorted(nums), 0, len(nums)
    for index in range(2, n):
        left, right = 0, index - 1
        while left < right:
            if nums[left] + nums[right] > nums[index]:
                count += (right - left)
                right -= 1
            else:
                left += 1
    return count


if __name__ == '__main__':
    input_nums = [2, 2, 3, 4]
    print(triangle_number(input_nums))
