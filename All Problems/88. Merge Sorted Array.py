
def merge(nums1, m, nums2, n):
    del nums1[m:]
    del nums2[n:]
    nums1.extend(nums2)
    nums1.sort()


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)
