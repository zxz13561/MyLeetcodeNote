from datetime import datetime as dt


def k_weakest_rows(mat, k):
    new_dic = {}
    for index, sub_list in enumerate(mat):
        try:
            new_dic[index] = sub_list.index(0)
        except ValueError:
            new_dic[index] = len(sub_list)
    result = sorted(new_dic, key=new_dic.get)
    return result[:k]


if __name__ == '__main__':
    input_mat = [[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]]
    input_k = 3
    print(k_weakest_rows(input_mat, input_k))
    """
    for time in range(100):
        start = dt.now()
        search_matrix(input_matrix, input_target)
        duration = dt.now() - start
        print(str(time + 1) + ' Try : ' + str(duration.microseconds / 10000) + ' ms')
    """
