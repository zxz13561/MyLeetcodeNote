class Solution(object):
    def flood_fill(self, image, sr, sc, new_color):
        curr_color = image[sr][sc]
        if curr_color == new_color:
            return image
        self.dfs(image, sr, sc, new_color, curr_color)
        return image

    def dfs(self, image, sr, sc, new_color, curr_color):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != curr_color:
            return

        image[sr][sc] = new_color
        temp_arr = []
        for i in range(3):
            temp_arr.append([x for x in image[i]])
        temp_arr[sr][sc] = "c"
        print(temp_arr[0])
        print(temp_arr[1])
        print(temp_arr[2])
        print("---------------")
        self.dfs(image, sr - 1, sc, new_color, curr_color)  # going up
        print("pass up")
        self.dfs(image, sr + 1, sc, new_color, curr_color)  # going down
        print("pass down")
        self.dfs(image, sr, sc - 1, new_color, curr_color)  # going left
        print("pass left")
        self.dfs(image, sr, sc + 1, new_color, curr_color)  # going right
        print("pass right")


if __name__ == '__main__':
    input_image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    input_sr = 1
    input_sc = 1
    input_newColor = 2
    call_solution = Solution()
    print(call_solution.flood_fill(input_image, input_sr, input_sc, input_newColor))
