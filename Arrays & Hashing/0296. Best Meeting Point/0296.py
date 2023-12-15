class Solution:

    def distance(self, x1, y1, x2, y2):
        return (abs(x2 - x1) + abs(y2 - y1))

    def minTotalDistance(self, grid: List[List[int]]) -> int:
        x = y = 0
        res = 0
        x_list = []
        y_list = []
        median = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    x_list.append(i)
                    y_list.append(j)
    
        x_list.sort()
        y_list.sort()
        if len(x_list) % 2 == 1:
            median = len(x_list) // 2
        else:
            median = (len(x_list) + 1) // 2
        
        for i in range(len(x_list)):
            res += self.distance(x_list[i], y_list[i], x_list[median], y_list[median])

        return res