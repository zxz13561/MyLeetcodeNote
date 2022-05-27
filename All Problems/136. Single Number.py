from functools import reduce
from operator import xor


class Solution(object):
    def single_number(self, nums):
        count_dic = {}
        for num in nums:
            if num not in count_dic:
                count_dic[num] = 1
            else:
                count_dic[num] += 1

        return min(count_dic, key=count_dic.get)

    def single_number2(self, nums):
        nums = sorted(nums)
        i = len(nums) - 1
        while i >= 0:
            if nums.index(nums[i]) == i:
                return nums[i]
            i = min(nums.index(nums[i]), i)
            i -= 1


    def one_liner(self, nums):
        return reduce(xor, nums)


if __name__ == '__main__':
    input_nums = [2, 2, 1]
    run = Solution()
    print(run.single_number2(input_nums))
