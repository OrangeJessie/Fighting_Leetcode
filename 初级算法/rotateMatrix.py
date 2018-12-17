class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        c_l = int(l/2)
        for i in range(c_l):
            for j in range(l):
                col = j
                row = l-1-i
                a = matrix[row][col]
                matrix[row][col] = matrix[i][j]
                matrix[i][j] = a
        for i in range(l):
            c_l2 = i + 1
            for j in range(c_l2):
                col = i
                row = j
                a = matrix[row][col]
                matrix[row][col] = matrix[i][j]
                matrix[i][j] = a


s = Solution()
mat = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]]
s.rotate(mat)
print(mat)
