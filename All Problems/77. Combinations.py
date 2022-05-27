class Solution(object):
    def combine(self, n, k):
        combs = [[]]
        r_list = []
        for _ in range(k):
            for c in combs:
                for i in range(1, c[0] if c else n + 1):
                    combs = [[i] + c]
                    if _ == k - 1:
                        r_list.append(combs[0])
                    print(combs)
        """
        for _ in range(k):
            combs = [[i] + c for c in combs for i in range(1, c[0] if c else n + 1)]
        """
        return r_list


if __name__ == '__main__':
    run = Solution()
    print(run.combine(4, 2))
