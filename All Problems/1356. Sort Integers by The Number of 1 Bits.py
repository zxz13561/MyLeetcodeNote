
class Solution(object):
    def sortByBits(self, arr):
        return sorted([n for n in sorted(arr)], key=lambda x: format(x, 'b').count('1'))


if __name__ == '__main__':
    i_arr = [2, 4, 8, 16, 64, 32, 256, 128]

    run = Solution()
    print(run.sortByBits(i_arr))
