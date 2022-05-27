class Solution(object):
    def shuffle(self, nums, n):
        r_list = []
        for i in range(n):
            r_list.append(nums[i])
            r_list.append(nums[n + i])
        return r_list

    def shuffle2(self, nums, n):
        return [y for x in zip(nums[:n], nums[n:]) for y in x]


if __name__ == '__main__':
    input_nums = [1, 2, 3, 4, 4, 3, 2, 1]
    input_n = 4
    run = Solution()
    print(run.shuffle2(input_nums, input_n))
