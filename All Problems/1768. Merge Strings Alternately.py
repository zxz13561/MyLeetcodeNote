class Solution(object):
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        ret_str = ""
        while i <= max(len(word1), len(word2)):
            ret_str += word1[i] if i < len(word1) else ""
            ret_str += word2[i] if i < len(word2) else ""
            i += 1

        return ret_str


if __name__ == '__main__':
    w1 = "abcd"
    w2 = "pq"

    run = Solution()
    print(run.mergeAlternately(w1, w2))
