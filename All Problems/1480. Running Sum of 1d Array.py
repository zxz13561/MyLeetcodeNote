class Solution(object):
    def running_sum(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        return nums

    def running_sum2(self, nums):
        return [sum(nums[0:i+1]) for i in range(len(nums))]


if __name__ == '__main__':
    input_nums = [1, 2, 3, 4]
    run = Solution()
    print(run.running_sum2(input_nums))
