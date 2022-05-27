class Solution(object):
    def permute(self, nums):
        global re_list
        re_list = []
        list_length = len(input_list)
        self.recursion_func(nums, 0, list_length)
        return re_list

    def recursion_func(self, nums, l, list_length):
        if l == list_length:
            re_list.append([i for i in nums])
        else:
            for i in range(l, list_length):
                nums[l], nums[i] = nums[i], nums[l]
                print(i, l, nums)
                self.recursion_func(nums, l + 1, list_length)
                nums[l], nums[i] = nums[i], nums[l]



if __name__ == '__main__':
    input_list = [1, 2, 3, 4]
    run = Solution()
    print(run.permute(input_list))


