class Solution(object):
    def rangeSumBST(self, nums1, nums2) -> int:
        dis = 0
        s_p = 0
        for i1, n1 in enumerate(nums1):
            if i1 == 762:
                print(n1)
            s_p += self.search_i(nums2[s_p:], n1)
            dis = max(dis, s_p - i1)
        return dis

    def search_i(self, nums, t):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] >= t:
                l = m + 1
            else:
                r = m - 1
        return r if r > 0 else 0


if __name__ == '__main__':
    run = Solution()
    print(run.maxDistance(i_nums1, i_nums2))
    print(len(i_nums2))
