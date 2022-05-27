class Solution(object):
    def generate(self, numRows):
        re_list = []
        save_list = []
        while numRows > 0:
            save_list = [save_list[i] + save_list[i - 1] if i > 0 else save_list[i] for i in range(len(save_list))] + [1]
            re_list.append(list(save_list))
            numRows -= 1
        return re_list


if __name__ == '__main__':
    input_numRows = 5
    run = Solution()
    print(run.generate(input_numRows))
