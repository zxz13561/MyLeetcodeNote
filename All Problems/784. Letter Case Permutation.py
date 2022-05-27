class Solution(object):
    def letter_case_permute(self, s):
        global re_list
        s = s.lower()
        s_list, re_list = list(s), [s]
        list_length = len(s_list)
        if list_length == 1 and isinstance(s, int):
            re_list.append(s.upper())
            return re_list
        self.recursion_func(s_list, 0, list_length)
        return re_list

    def recursion_func(self, nums, l, list_length):
        chk_str = str.join('', nums)
        if chk_str not in re_list:
            re_list.append(str.join('', nums))

        for i in range(l, list_length):
            nums[l], nums[i] = nums[l].lower(), nums[i].upper()
            print(i, l, nums)
            self.recursion_func(nums, l + 1, list_length)
            nums[l], nums[i] = nums[l].lower(), nums[i].lower()

    def soluion02(self, s):
        def backtrack(sub="", i=0):
            if len(sub) == len(s):
                res.append(sub)
            else:
                if s[i].isalpha():
                    backtrack(sub + s[i].swapcase(), i + 1)
                backtrack(sub + s[i], i + 1)

        res = []
        backtrack()
        return res


if __name__ == '__main__':
    input_s = "kMsG6bHsg"
    run = Solution()

    expect_list = ["dntj", "dntJ", "dnTj", "dnTJ", "dNtj", "dNtJ", "dNTj", "dNTJ", "Dntj", "DntJ", "DnTj", "DnTJ",
                   "DNtj", "DNtJ", "DNTj", "DNTJ"]

    output_list = run.letter_case_permute(input_s)

    for chk in output_list:
        if chk not in expect_list:
            print(chk)
