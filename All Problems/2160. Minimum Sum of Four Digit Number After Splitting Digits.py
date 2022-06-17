class Solution(object):
    def minimum_sum(self, num):
        n_list = sorted(list(str(num)))
        return int(str.join("", n_list[0] + n_list[3])) + int(str.join("", n_list[1] + n_list[2]))


if __name__ == '__main__':
    input_num = 2687
    run = Solution()
    print(run.minimum_sum(input_num))
