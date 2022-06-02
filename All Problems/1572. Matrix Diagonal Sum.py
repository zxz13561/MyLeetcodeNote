class Solution(object):
    def diagonalSum(self, mat) -> int:
        mat_len = len(mat)
        if mat_len == 1:
            return mat[0][0]

        p_i, ret_val = 0, 0
        while p_i <= mat_len - 1:
            ret_val += mat[p_i][p_i] + mat[-1 + p_i * -1][p_i]
            p_i += 1

        return ret_val if mat_len % 2 == 0 else ret_val - mat[mat_len // 2][mat_len // 2]


if __name__ == '__main__':
    i_mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]

    run = Solution()
    print(run.diagonalSum(i_mat))
