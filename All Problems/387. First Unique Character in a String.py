from math import inf


class Solution(object):
    def firstUniqChar(self, s):
        s_dic = {}
        for s_chr in s:
            if s_chr not in s_dic:
                s_dic[s_chr] = 1
            else:
                s_dic[s_chr] += 1
        try:
            return s.index(list(s_dic.keys())[list(s_dic.values()).index(1)])
        except ValueError:
            return -1

    def faster_solution(self, s):
        res = inf
        for i in range(26):
            c = chr(i + ord("a"))
            idx = s.find(c)
            if idx > -1 and idx == s.rfind(c):
                res = min(res, idx)
        return res if res < inf else -1


if __name__ == '__main__':
    input_s = "ddcc"
    run = Solution()
    print(run.faster_solution(input_s))
