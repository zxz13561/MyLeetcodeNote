from datetime import datetime as dt


def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()
    result_list = []
    for num in nums1:
        l_limit = 0
        r_limit = len(nums2) - 1
        while l_limit <= r_limit:
            mid = l_limit + (r_limit - l_limit) // 2
            if num == nums2[mid]:
                result_list.append(num)
                nums2.pop(mid)
                break
            elif num > nums2[mid]:
                l_limit = mid + 1
            else:
                r_limit = mid - 1
    return result_list


if __name__ == '__main__':
    input_nums1 = [4, 9, 5]
    input_nums2 = [9, 4, 9, 8, 4]
    print(intersect(input_nums1, input_nums2))
    """
    for time in range(100):
        start = dt.now()
        search_matrix(input_matrix, input_target)
        duration = dt.now() - start
        print(str(time + 1) + ' Try : ' + str(duration.microseconds / 10000) + ' ms')
    """
