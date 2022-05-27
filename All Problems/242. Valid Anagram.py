import collections


class Solution(object):
    def isAnagram(self, s, t) -> bool:
        return collections.Counter(s) == collections.Counter(t)


if __name__ == '__main__':
    input_s = "abc"
    input_t = "cba"
    run = Solution()
    print(run.isAnagram(input_s, input_t))
