class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)
        val_list = nums[0:3]

        for num in nums[3:]:
            if self.is_vaild(val_list):
                return sum(val_list)
            else:
                val_list.remove(max(val_list))
                val_list.append(num)

        return sum(val_list) if self.is_vaild(val_list) else 0

    def is_vaild(self, t_list):
        t_list.sort()
        if sum(t_list[:2]) > t_list[-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    i_nums = [2, 1, 2]

    run = Solution()
    print(run.largestPerimeter(i_nums))
