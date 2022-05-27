class Solution(object):
    def minimum_total(self, triangle):
        if not triangle:
            return
        res = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            print("triangle len : {} ".format(len(triangle[i])))
            for j in range(len(triangle[i])):
                print(res[j], min(res[j], res[j + 1]), triangle[i][j])
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
                for ele in triangle:
                    print(ele)
        return res[0]

    def fast_solution(self, triangle):
        m = len(triangle)

        for i in range(1, m):
            for j in range(i + 1):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == i:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])
        return min(triangle[-1])


if __name__ == '__main__':
    input_triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    run = Solution()
    mininum_num = run.fast_solution(input_triangle)
    print(mininum_num)
