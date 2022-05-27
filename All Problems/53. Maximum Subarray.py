class Solution(object):
    def maxSubArray(self, nums) -> int:
        max_so_far = nums[0]
        current_sum = nums[0]

        if len(nums) == 1:
            return max_so_far

        for n in nums[1:]:
            current_sum += n
            if n > current_sum:
                current_sum = n
            if current_sum > max_so_far:
                max_so_far = current_sum

        return max_so_far


if __name__ == '__main__':
    input_arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    run = Solution()
    result = run.maxSubArray(input_arr)
    print(result)
