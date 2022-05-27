def find_the_distance_value(d):
    """
    arr1 = [-803, 715, -224, 909, 121, -296, 872, 807, 715, 407, 94, -8, 572, 90, -520, -867, 485, -918, -827, -728,
            -653, -659, 865, 102, -564, -452, 554, -320, 229, 36, 722, -478, -247, -307, -304, -767, -404, -519, 776,
            933, 236, 596, 954, 464]
    arr2 = [817, 1, -723, 187, 128, 577, -787, -344, -920, -168, -851, -222, 773, 614, -699, 696, -744, -302, -766,
            259, 203, 601, 896, -226, -844, 168, 126, -542, 159, -833, 950, -454, -253, 824, -395, 155, 94, 894, -766,
            -63, 836, -433, -780, 611, -907, 695, -395, -975, 256, 373, -971, -813, -154, -765, 691, 812, 617, -919,
            -616, -510, 608, 201, -138, -669, -764, -77, -658, 394, -506, -675, 523, 730, -790, -109, 865, 975, -226,
            651, 987, 111, 862, 675, -398, 126, -482, 457, -24, -356, -795, -575, 335, -350, -919, -945, -979, 611]
    """
    arr1 = [2, 1, 100, 3]
    arr2 = [-5, -2, 10, -3, 7]

    count_result = 0
    arr2.sort()

    for num in arr1:
        l_limit = 0
        r_limit = len(arr2) - 1
        num_ng = False

        while l_limit <= r_limit:
            mid = l_limit + (r_limit - l_limit) // 2
            if num == arr2[mid]:
                num_ng = True
                break
            elif num > arr2[mid]:
                l_limit = mid + 1
            else:
                r_limit = mid - 1

        if l_limit > len(arr2) - 1:
            l_limit = len(arr2) - 1
        l_num = arr2[l_limit]
        r_num = arr2[r_limit]
        left_dis = abs(num - l_num)
        right_dis = abs(num - r_num)
        if not num_ng and left_dis > d and right_dis > d:
            count_result += 1
    return count_result


if __name__ == '__main__':
    input_d = 6
    print(find_the_distance_value(input_d))
