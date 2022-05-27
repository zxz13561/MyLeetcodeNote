class Solution(object):
    def minimum_sum(self, nums) -> int:
        for i in range(1, len(str(nums))):
            shift = 10 ** i
            new1, new2 = nums // shift, nums % shift
            print(new1, new2, new1 + new2)


if __name__ == '__main__':
    input_num = 2932
    run = Solution()
    print(run.minimum_sum(input_num))
