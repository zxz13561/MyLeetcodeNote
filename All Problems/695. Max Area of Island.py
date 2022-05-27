class Solution(object):
    def max_area_of_island(self, grid):
        temp_list = [0]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    temp_list.append(0)
                    self.dfs(grid, i, j, temp_list)
        return max(temp_list)

    def max_area_of_island_2(self, grid):
        temp_list = [0]
        for i in range(len(grid)):
            try:
                while True:
                    j = grid[i].index(1)
                    temp_list.append(0)
                    self.dfs(grid, i, j, temp_list)
            except ValueError:
                continue
        return max(temp_list)

    def dfs(self, grid, i, j, temp_list):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return

        grid[i][j] = 2
        temp_list[-1] += 1
        self.dfs(grid, i - 1, j, temp_list)
        self.dfs(grid, i + 1, j, temp_list)
        self.dfs(grid, i, j - 1, temp_list)
        self.dfs(grid, i, j + 1, temp_list)


if __name__ == '__main__':

    input_grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                  [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                  [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    input_grid_1 = [[0, 0, 0, 0, 0, 0, 0, 0]]
    call_method = Solution()
    print(call_method.max_area_of_island_2(input_grid))
