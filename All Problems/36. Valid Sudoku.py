import collections


class Solution(object):
    def is_valid_sudoku(self, board):
        seen = sum(([(c, i), (j, c), (i / 3, j / 3, c)]
                    for i, row in enumerate(board)
                    for j, c in enumerate(row)
                    if c != '.'), [])
        for i in range(0, 82, 9):
            print(seen[i:i + 9])

        print(set(seen))
        return len(seen) == len(set(seen))

    def fast_92_percent(self, board):
        N = 9
        rowSet = [set() for _ in range(N)]
        colSet = [set() for _ in range(N)]
        squareSet = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                if board[r][c] == ".": continue
                sr, sc = r // 3, c // 3
                sPos = sr * 3 + sc
                if board[r][c] in rowSet[r] or board[r][c] in colSet[c] or board[r][c] in squareSet[sPos]:
                    return False
                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                squareSet[sPos].add(board[r][c])

        return True


if __name__ == '__main__':
    input_board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                   ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                   [".", "9", "8", ".", ".", ".", ".", "6", "."],
                   ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                   ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                   ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                   [".", "6", ".", ".", ".", ".", "2", "8", "."],
                   [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                   [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    run = Solution()
    print(run.is_valid_sudoku(input_board))
