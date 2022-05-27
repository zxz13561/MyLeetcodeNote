
def search(nums, target) -> int:
    border_l = 0
    border_r = len(nums) - 1

    while border_l <= border_r :
        mid_index = (border_l + border_r) // 2
        if nums[mid_index] > target :
            border_r = mid_index - 1
        elif nums[mid_index] < target :
            border_l = mid_index + 1
        else:
            return mid_index
    return -1


if __name__ == '__main__':
    input_nums = [-1, 0, 3, 5, 9, 12]
    input_target = 13

    print(search(input_nums, input_target))
