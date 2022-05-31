class Solution(object):
    def checkStraightLine(self, coordinates):
        if len(coordinates) == 2:
            return True

        coordinates.sort()
        f_p, s_p = coordinates[0], coordinates[1]
        m = self.find_m(f_p, s_p)

        if m != 0:
            for i, p in enumerate(coordinates[2:]):
                prv_p = coordinates[i + 1]
                if self.find_m(prv_p, p) != m:
                    return False
            return True
        elif f_p[0] - s_p[0] == 0:
            x_line = f_p[0]
            for p in coordinates[2:]:
                if p[0] != x_line:
                    return False
            return True
        else:
            y_line = f_p[1]
            for p in coordinates[2:]:
                if p[1] != y_line:
                    return False
            return True

    def find_m(self, p1, p2):
        if p2[1] - p1[1] != 0 and p2[0] - p1[0] != 0:
            return (p2[1] - p1[1]) / (p2[0] - p1[0])
        else:
            return 0


if __name__ == '__main__':
    i_coordinates = [[1, 1], [2, 2], [2, 1], [3, 2]]

    run = Solution()
    print(run.checkStraightLine(i_coordinates))
