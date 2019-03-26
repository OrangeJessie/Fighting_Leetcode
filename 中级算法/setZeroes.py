# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
# 输入:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]


# 记录置零的行号和列号是m+n空间复杂度的算法
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        row = len(matrix)
        column = len(matrix[0])
        zero_r = []
        # 置零行，用字符代替置零位
        for i in range(row):
            if 0 in matrix[i]:
                for j in range(column):
                    if matrix[i][j] != 0:
                        matrix[i][j] = 'a'
        # 置零列
        for j in range(column):
            new = []
            for i in range(row):
                new.append(matrix[i][j])
            if 0 in new:
                for i in range(row):
                    matrix[i][j] = 0

        for i in range(row):
            for j in range(column):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0

    # 以第一行第一列为标志行列
    def setZeroes2(self, matrix):
        if len(matrix) == 0:
            return

        colFlag, rowFlag, rows, cols = 1, 1, len(matrix), len(matrix[0])

        # Recording whether the first row and the first col contain 0
        for i in range(cols):
            if matrix[0][i] == 0:
                colFlag = 0

        for i in range(rows):
            if matrix[i][0] == 0:
                rowFlag = 0

        # Start from the second row and the second col
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # Set zero from the bottom
        for i in range(rows-1, 0, -1):
            for j in range(cols-1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Check the row and the col
        if colFlag == 0:
            for i in range(cols):
                matrix[0][i] = 0
        if rowFlag == 0:
            for i in range(rows):
                matrix[i][0] = 0
