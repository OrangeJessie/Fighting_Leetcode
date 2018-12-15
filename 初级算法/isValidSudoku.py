class Solution:
    # 注意在python中数组列的读取不能直接使用b[:, :], 而在numpy中可以
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        hight = 9
        weight = 9
        for i in range(hight):
            h = board[i]
            c = h.count('.')
            l1 = len(set(h))
            l2 = len(h) - c + 1
            if l1 != l2:
                return False
        for j in range(weight):
            w = [x[j] for x in board]
            c = w.count('.')
            if len(set(w)) != len(w)-c+1:
                return False
        for i in range(3):
            for j in range(3):
                sq = []
                for i2 in range(3):
                    sq = sq+board[3*i+i2][3*j:3*(j+1)]
                c = sq.count('.')
                real_len = len(set(sq))
                list_len = len(sq)
                if real_len != list_len-c+1:
                    return False
        return True


s = Solution()
b = [[".",".","4",".",".",".","6","3","."],
     [".",".",".",".",".",".",".",".","."],
     ["5",".",".",".",".",".",".","9","."],
     [".",".",".","5","6",".",".",".","."],
     ["4",".","3",".",".",".",".",".","1"],
     [".",".",".","7",".",".",".",".","."],
     [".",".",".","5",".",".",".",".","."],
     [".",".",".",".",".",".",".",".","."],
     [".",".",".",".",".",".",".",".","."]]
print(s.isValidSudoku(b))
