from collections import Counter


class Solution(object):
    def areAlmostEqual(self, s1, s2) -> bool:
        if Counter(s1) != Counter(s2):
            return False

        swap_dic = {}
        already_swap = False
        for i, c in enumerate(s1[:]):
            if len(swap_dic) >= 2:
                return False

            if c != s2[i]:
                if not already_swap:
                    swap_dic[s2[i]] = c
                    already_swap = True
                elif c not in swap_dic:
                    return False
                elif c in swap_dic and swap_dic[c] != s2[i]:
                    return False

        return True

    def faster(self, s1, s2):
        diff = [[x, y] for x, y in zip(s1, s2) if x != y]
        return not diff or len(diff) == 2 and diff[0][::-1] == diff[1]


if __name__ == '__main__':
    i_s1 = "bank"
    i_s2 = "kanb"

    run = Solution()
    print(run.areAlmostEqual(i_s1, i_s2))
