class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        j_dic = {j: 1 for j in jewels}
        return sum([j_dic[s] if s in j_dic else 0 for s in stones])


if __name__ == '__main__':
    i_jewels, i_stones = "aA", "aAAbbbb"
    run = Solution()
    print(run.numJewelsInStones(i_jewels, i_stones))
