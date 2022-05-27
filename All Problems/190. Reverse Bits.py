class Solution(object):
    def reverse_bits(self, n):
        return int('0b' + format(n, '032b')[::-1], 2)


if __name__ == '__main__':
    input_n = 43261596
    run = Solution()
    print(run.reverse_bits(input_n))
