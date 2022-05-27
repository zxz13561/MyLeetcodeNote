class Solution(object):
    def is_power_of_two(self, n: int) -> bool:
        n = abs(n)
        if n < 0:
            return False
        if n > 1 and n % 2 > 0 :
            return False

        bin_list = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]

        if n in bin_list:
            return True

        for i in range(0, len(bin_list) - 1):
            while n >= 1:
                if n >= bin_list[i]:
                    n = n / bin_list[i]
                elif n < bin_list[i]:
                    break
        if n == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    input_n = -1
    run = Solution()
    print(run.is_power_of_two(input_n))
