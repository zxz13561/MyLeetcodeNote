class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        ret_sum = sum(arr)

        if len(arr) <= 2:
            return ret_sum

        odd_len = 3
        while odd_len <= len(arr):
            start_i = 0
            end_i = odd_len
            for i in range(len(arr[odd_len - 1:])):
                ret_sum += sum(arr[start_i:end_i])
                start_i += 1
                end_i += 1

            odd_len += 2

        return ret_sum


if __name__ == '__main__':
    a1 = [1, 4, 2, 5, 3]

    run = Solution()
    print(run.sumOddLengthSubarrays(a1))
