import math


class Solution(object):
    def nearestValidPoint(self, x, y, points):
        vai_points = [point for point in points if point[0] == x or point[1] == y]

        if len(vai_points) == 0:
            return -1
        elif len(vai_points) == 1:
            return points.index(vai_points[0])

        val_list = {points.index(p): abs(p[0] - x) + abs(p[1] - y) for p in vai_points}
        return [k for k, v in val_list.items() if v == min(val_list.values())][0]

    def little_faster(self, x, y, points):
        minDist = math.inf
        ans = -1
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                manDist = abs(points[i][0] - x) + abs(points[i][1] - y)
                if manDist < minDist:
                    ans = i
                    minDist = manDist
        return ans

if __name__ == '__main__':
    i_points = [[25, 45], [60, 19], [11, 38], [32, 22], [1, 24], [26, 25], [52, 36], [45, 54], [45, 30], [45, 39],
                [39, 38],
                [25, 38], [39, 57], [47, 51], [47, 49], [37, 21], [16, 43], [53, 33], [10, 50], [30, 29], [3, 31],
                [45, 26],
                [22, 40], [2, 31], [57, 42], [25, 42], [37, 13], [13, 54], [17, 5], [50, 32]]
    i_x = 28
    i_y = 51

    run = Solution()
    print(run.nearestValidPoint(i_x, i_y, i_points))
