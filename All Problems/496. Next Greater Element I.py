class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ret = []
        for num in nums1:
            i = nums2.index(num)
            for n in nums2[i:]:
                if n > num:
                    ret.append(n)
                    break
                if n == nums2[-1]:
                    ret.append(-1)

        return ret

    def faster(self, nums1, nums2):
        nextGreaterDict = {}
        monoStack = []

        for num in nums2:
            while monoStack and num > monoStack[-1]:
                nextGreaterDict[monoStack.pop()] = num
            monoStack.append(num)

        for i, num in enumerate(nums1):
            nums1[i] = nextGreaterDict.get(num, -1)

        return nums1


if __name__ == '__main__':
    n1 = [4, 1, 2]
    n2 = [1, 3, 4, 2]

    run = Solution()
    print(run.faster(n1, n2))
