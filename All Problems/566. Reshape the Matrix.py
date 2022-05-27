class Solution(object):
    def matrixReshape(self, mat, r, c):
        to_1d = []
        for m in mat:
            to_1d += m

        if r * c != len(to_1d):
            return mat

        div_hor = len(to_1d) // r + 1 if len(to_1d) % r > 0 else len(to_1d) // r
        begin, end = 0, div_hor
        r_list = []
        for i in range(r):
            r_list.append(to_1d[begin:end])
            begin, end = end, end + c
        return r_list


if __name__ == '__main__':
    run = Solution()
    print(run.matrixReshape([[1, 2], [3, 4]], 4, 4))
