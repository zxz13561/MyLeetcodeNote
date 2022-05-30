class Solution(object):
    def canMakeArithmeticProgression(self, arr) -> bool:
        if len(arr) == 2:
            return True

        arr.sort()
        for i in range(len(arr) - 2):
            if arr[i + 1] - arr[i] != arr[i + 2] - arr[i + 1]:
                return False

        return True


if __name__ == '__main__':
    i_arr = [3, 5, 1]

    run = Solution()
    print(run.canMakeArithmeticProgression(i_arr))
