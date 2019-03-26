# 岛屿的个数
# 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。
# 一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
#
# 示例 1:
# 输入:
# 11110
# 11010
# 11000
# 00000
#
# 输出: 1


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        lr = len(grid)
        lc = len(grid[0])
        new_grid = [['0' for i in range(lc+2)]]
        for row in grid:
            new_grid.append(['0']+row+['0'])
        new_grid.append(['0' for i in range(lc+2)])
        count = 0
        for i in range(lr+2):
            for j in range(lc+2):
                if new_grid[i][j] == '1':
                    self.searchIland(new_grid, i, j)
                    count += 1
        return count

    def searchIland(self, grid, index_r, index_c):
        if grid[index_r][index_c] == '0':
            return
        grid[index_r][index_c] = '0'
        self.searchIland(grid, index_r-1, index_c)
        self.searchIland(grid, index_r+1, index_c)
        self.searchIland(grid, index_r, index_c-1)
        self.searchIland(grid, index_r, index_c+1)
