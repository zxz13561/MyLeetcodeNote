from collections import Counter, deque


def check_inclusion(s1, s2):
    cntr, w, match = Counter(s1), len(s1), 0

    for i in range(len(s2)):
        # check char is in s1 counter
        if s2[i] in cntr:
            if not cntr[s2[i]]:
                match -= 1
            cntr[s2[i]] -= 1
            if not cntr[s2[i]]:
                match += 1

        #
        if i >= w and s2[i - w] in cntr:
            if not cntr[s2[i - w]]:
                match -= 1
            cntr[s2[i - w]] += 1
            if not cntr[s2[i - w]]:
                match += 1

        if match == len(cntr):
            return True

    return False


def check_inclusion_t(s1, s2):
    check_list = []
    for i in range(len(s2)):
        if s2[i] in s1 and s2[i] not in check_list:
            check_list.append(s2[i])
        elif s2[i] in check_list:
            continue
        else:
            check_list = []
        if len(check_list) == len(s1):
            return True
        print(check_list)
    return False

def fastes_solution(s1, s2):
    n1, n2 = len(s1), len(s2)
    if n1 > n2: return False
    tbl = {}
    for i in range(26):
        tbl[chr(ord('a') + i)] = 1 << (i + 1)
    summ1 = summ2 = 0
    queue = deque()
    count1 = Counter(s1)
    for i in range(n1):
        summ1 += tbl[s1[i]]
        summ2 += tbl[s2[i]]
        queue.append(s2[i])
    if summ1 == summ2:
        if Counter(queue) == count1:
            return True
    for i in range(n1, n2):
        queue.popleft()
        queue.append(s2[i])
        summ2 -= tbl[s2[i - n1]]
        summ2 += tbl[s2[i]]
        if summ1 == summ2:
            if Counter(queue) == count1:
                return True
    return False


if __name__ == '__main__':
    input_s1 = "hello"
    input_s2 = "ooolleooolleh"
    print(check_inclusion_t(input_s1, input_s2))
