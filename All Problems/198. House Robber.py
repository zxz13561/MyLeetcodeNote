from datetime import datetime as dt


def rob(nums):
    prev2_house = 0
    prev_house = 0
    current_house = 0
    for value in nums:
        current_value = max(prev_house, value + prev2_house)
        prev2_house = prev_house
        prev_house = current_value
    return current_value


def rob2(nums):
    memo = [0 for _ in range(len(nums)+1)]
    memo[0], memo[1] = 0, nums[0]
    for i in range(1, len(nums)):
        curr = memo[i-1] + nums[i]
        pre = memo[i]
        memo[i+1] = (max(pre, curr))
    return memo[len(nums)]


if __name__ == '__main__':
    input_nums = [5, 100, 2, 1]
    print(rob(input_nums))
    """
    for time in range(100):
        start = dt.now()
        search_matrix(input_matrix, input_target)
        duration = dt.now() - start
        print(str(time + 1) + ' Try : ' + str(duration.microseconds / 10000) + ' ms')
    """
