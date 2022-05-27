class Solution(object):
    def hamming_weight(self, n):
        return len([num for num in list(bin(n)) if num == '1'])

    def faster_solution(self, n):
        ans = 0
        # print(str(bin(n)))
        for i in str(bin(n)):
            if i == "1":
                ans += 1
        return ans


if __name__ == '__main__':
    input_n = 15
    run = Solution()
    print(run.hamming_weight(input_n))