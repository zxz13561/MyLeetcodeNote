
def find_kth_positive(arr, k):
    l_limit = 0
    r_limit = len(arr) - 1

    while l_limit <= r_limit:
        mid = l_limit + (r_limit - l_limit) // 2
        if k > arr[mid] - mid - 1:
            l_limit = mid + 1
        else:
            r_limit = mid - 1
    return l_limit + k


if __name__ == '__main__':
    input_nums = [2, 3, 4, 7, 11, 12]
    input_k = 7

    print(find_kth_positive(input_nums, input_k))
