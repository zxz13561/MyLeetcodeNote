
def peak_index_in_mountain_array(arr) -> int:
    border_l = 1
    border_r = len(arr) - 2

    while border_l <= border_r:
        mid = border_l + (border_r - border_l) // 2
        if(arr[mid] > arr[mid + 1]) & (arr[mid] > arr[mid - 1]):
            return mid
        elif arr[mid] < arr[mid + 1]:
            border_l = mid + 1
        else:
            border_r = mid - 1
    return border_l


if __name__ == '__main__':
    input_nums = [0, 2, 3, 1, 0]

    print(peak_index_in_mountain_array(input_nums))
