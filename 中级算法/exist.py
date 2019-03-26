# 单词搜索
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
# 示例:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        lr = len(board)
        lc = len(board[0])
        have_board = [[0 for k in range(lc)] for k in range(lr)]
        symbol = []
        for i in range(lr):
            for j in range(lc):
                if board[i][j] == word[0]:
                    if self.dfs(board, word, have_board, i, j, symbol):
                        return True
        return False

    def dfs(self, board, word, have_board, index_r, index_c, symbol):
        if not word:
            return True
        if index_r >= len(board) or index_c >= len(board[0]) or index_r < 0 or index_c < 0:
            return False
        if board[index_r][index_c] != word[0]:
            return False
        if have_board[index_r][index_c]:
            return False
        have_board[index_r][index_c] = 1
        result = self.dfs(board, word[1:], have_board, index_r-1, index_c, symbol) or \
                self.dfs(board, word[1:], have_board, index_r+1, index_c, symbol) or \
                self.dfs(board, word[1:], have_board, index_r, index_c-1, symbol) or \
                self.dfs(board, word[1:], have_board, index_r, index_c+1, symbol)
        have_board[index_r][index_c] = 0
        return result
