class Solution:
    def generate(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return []
        elif rowIndex == 1:
            return [[1]]
        elif rowIndex == 2:
            return [[1], [1, 1]]
        row = [[1], [1, 1]]
        for i in range(3, rowIndex+1):
            every_row = []
            for j in range(i):
                if j == 0 or j == i-1:
                    every_row.append(1)
                else:
                    every_row.append(row[i-2][j-1] + row[i-2][j])
            row.append(every_row)
        return row
