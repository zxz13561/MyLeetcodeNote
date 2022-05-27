from collections import Counter


def sliding_window(nums, k):
    window = nums[:k]
    max_sum = sum(window)
    for i in range(len(nums) - k):
        total_sum = max_sum - nums[i] + nums[i + k]
        max_sum = max(total_sum, max_sum)
    return max_sum


if __name__ == '__main__':
    input_nums = [4, 2, 10, 3, 20]
    input_k = 2
    print(sliding_window(input_nums, input_k))
