
def search_insert(nums, target) -> int:
    border_l = 0
    border_r = len(nums) - 1

    while border_l <= border_r:
        mid_index = border_l + (border_r - border_l) // 2
        if nums[mid_index] == target:
            return mid_index
        elif nums[mid_index] > target:
            border_r = mid_index - 1
        else:
            border_l = mid_index + 1
    return border_l


if __name__ == '__main__':
    input_nums = [1, 3, 5, 6]
    input_target = 2

    print(search_insert(input_nums, input_target))
