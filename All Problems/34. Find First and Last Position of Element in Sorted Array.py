def search_range(nums, target):
    ans_list = [-1, -1]
    if not nums:
        return ans_list

    border_l = 0
    border_r = len(nums) - 1
    l_limit = False
    r_limit = False

    while border_l <= border_r:
        mid = border_l + (border_r - border_l) // 2
        if target == nums[mid]:
            l_index = mid
            r_index = mid
            ans_list = [l_index, r_index]
            while (not l_limit) or (not r_limit):
                if not l_limit and (len(nums) - 1) >= l_index >= 0 and nums[l_index] == target:
                    ans_list[0] = l_index
                    l_index = l_index - 1
                else:
                    l_limit = True

                if not r_limit and (len(nums) - 1) >= r_index >= 0 and nums[r_index] == target:
                    ans_list[1] = r_index
                    r_index = r_index + 1
                else:
                    r_limit = True

            return ans_list

        elif target > nums[mid]:
            border_l = mid + 1
        else:
            border_r = mid - 1
    return ans_list


if __name__ == '__main__':
    i_nums = [4, 5, 7, 7, 8, 8, 8, 8, 9, 10, 10, 11, 11, 12, 13, 14]
    # i_nums = []
    # i_nums = [1]
    # i_nums = [2, 2]
    i_target = 8

    print(search_range(i_nums, i_target))
