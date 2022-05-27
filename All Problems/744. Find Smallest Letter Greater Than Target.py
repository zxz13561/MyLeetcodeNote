
def next_greatest_letter(letters, target):
    ascii_list = [ord(s) for s in letters]
    ascii_list = list(set(ascii_list))
    ascii_list.sort()
    l_limit = 0
    r_limit = len(ascii_list) - 1
    list_len = len(ascii_list) - 1

    while l_limit <= r_limit:
        mid = l_limit + (r_limit - l_limit) // 2
        if ord(target) == ascii_list[mid]:
            if (mid + 1) <= list_len:
                return chr(ascii_list[mid + 1])
            else:
                return chr(ascii_list[0])
        elif ord(target) > ascii_list[mid]:
            l_limit = mid + 1
        else:
            r_limit = mid - 1
    if l_limit <= list_len:
        return chr(ascii_list[l_limit])
    else:
        return chr(ascii_list[0])


if __name__ == '__main__':
    i_letters = ["c", "f", "j"]
    i_target = "a"

    i_letters2 = ["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"]
    i_target2 = "e"
    print(next_greatest_letter(i_letters, i_target))
