import math
from collections import deque


class Solution(object):
    @staticmethod
    def oranges_rotting(grid):
        rotting_time = 0
        m, n = len(grid), len(grid[0])
        direction_list = [0, 1, 0, -1, 0]  # up, right, down, left

        r_list = []
        r_apple = deque([])
        count_flesh_apple = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    r_apple.append((r, c))
                elif grid[r][c] == 0:
                    continue
                else:
                    grid[r][c] = -1  # Marked as not processed yet!
                    count_flesh_apple += 1
        r_list.append(r_apple)

        # check is have rotten apple
        how_many_rotten = len(r_apple)
        if how_many_rotten == 0 and count_flesh_apple == 0:
            return 0

        for r_q in r_list:
            rotting_time += 1
            temp_q = deque([])
            while r_q:
                r, c = r_q.popleft()
                for i in range(4):
                    # check this block surrounding value
                    nr = r + direction_list[i]
                    nc = c + direction_list[i + 1]

                    # check is in matrix and already process
                    if nr < 0 or nr == m or nc < 0 or nc == n or grid[nr][nc] != -1:
                        continue

                    # deal with block
                    grid[nr][nc] = 2
                    count_flesh_apple -= 1

                    # append not process block index into queue
                    temp_q.append((nr, nc))
            if len(temp_q) >= 1:
                r_list.append(temp_q)

        if count_flesh_apple >= 1:
            return -1
        else:
            return rotting_time - 1


if __name__ == '__main__':
    run_test = Solution()
    """
    input_grid = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 2]
    ]
    """
    """
    input_grid = [
        [2, 0]
    ]
    """

    input_grid = [[1]]

    print(run_test.oranges_rotting(input_grid))
