from collections import deque


class Solution(object):
    @staticmethod
    def update_matrix(mat):
        showing_matrix = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        process_order = 1

        m, n = len(mat), len(mat[0])
        direction_list = [0, 1, 0, -1, 0]  # up, right, down, left

        q = deque([])
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1  # Marked as not processed yet!
        print(q)
        while q:
            r, c = q.popleft()
            showing_matrix[r][c] = process_order
            process_order += 1
            print("----------------")
            for ele_s in mat:
                print(ele_s)
            print("----------------")
            for i in range(4):
                # check this block surrounding value
                nr = r + direction_list[i]
                nc = c + direction_list[i + 1]

                # check is in matrix and already process
                if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1:
                    continue

                # deal with block
                print(nr, nc, mat[nr][nc])
                mat[nr][nc] = mat[r][c] + 1

                showing_matrix[nr][nc] = process_order
                process_order += 1
                print("----------------")
                for ele_s in mat:
                    print(ele_s)
                print("----------------")

                # append not process block index into queue
                q.append((nr, nc))
                print(q)
        return mat


if __name__ == '__main__':
    run_test = Solution()
    input_mat = [
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1]
    ]
    input_mat = run_test.update_matrix(input_mat)
    for ele in input_mat:
        print(ele)
