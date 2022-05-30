class Solution(object):
    def isHappy(self, n) -> bool:
        while True:
            if n < 5:
                return False if n != 1 else True

            n = sum([int(num)**2 for num in str(n)])

    def faster(self, n):
        visited = set()
        while n not in visited:
            visited.add(n)
            n = sum([int(i) ** 2 for i in str(n)])

        # print(visited)
        return n == 1


if __name__ == '__main__':
    i_n = 4

    run = Solution()
    print(run.isHappy(i_n))
