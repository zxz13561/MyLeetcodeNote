from collections import Counter


class Solution(object):
    def findTheDifference(self, s: str, t:str) -> str:
        return list(Counter(t) - Counter(s))[0]

    def faster(self, s, t):
        t_set = set(t)
        for char in t_set:
            if s.count(char) != t.count(char):  # use for [a, aa] situation
                return char


if __name__ == '__main__':
    s1 = "abcd"
    t1 = "abcde"

    run = Solution()
    print(run.faster(s1, t1))
