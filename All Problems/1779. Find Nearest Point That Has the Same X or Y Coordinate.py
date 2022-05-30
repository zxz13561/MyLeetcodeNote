import math


class Solution(object):
    def nearestValidPoint(self, x, y, points):
        val_index = -1
        re_val = math.inf
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                count_dis = abs(points[i][0] - x) + abs(points[i][1] - y)
                if count_dis < re_val:
                    val_index = i
                    re_val = count_dis

        return val_index


if __name__ == '__main__':
    i_points = [[8205, 8862]]
    i_x = 58
    i_y = 7837

    run = Solution()
    print(run.nearestValidPoint(i_x, i_y, i_points))
