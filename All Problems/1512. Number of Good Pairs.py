class Solution(object):
    def num_identical_pairs(self, nums) -> int:
        good_pairs = 0
        for i in range(len(nums) - 1):
            for val in nums[i+1:]:
                if val == nums[i]:
                    good_pairs += 1
        return good_pairs

    def num_identical_pairs2(self, nums) -> int:
        dic_map = {}
        count = 0
        for num in nums:
            if num not in dic_map:
                dic_map[num] = 1
            else:
                count += dic_map[num]
                dic_map[num] += 1

        return count


if __name__ == '__main__':
    input_nums = [1, 2, 3, 1, 1, 3]
    run = Solution()
    print(run.num_identical_pairs2(input_nums))
