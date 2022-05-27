
def rotate(nums, k):
    if 0 < k != len(nums) > 1:
        k = k - (k // len(nums)) * len(nums)
        nums[:] = nums[-k:] + nums[:-k]


if __name__ == '__main__':
    input_nums = [1, 3, 4, 5, 9, 10]
    input_k = 5

    rotate(input_nums, input_k)
    print(input_nums)
