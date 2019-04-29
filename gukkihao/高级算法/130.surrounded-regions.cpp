/*
 * @lc app=leetcode id=130 lang=cpp
 *
 * [130] Surrounded Regions
 */
class Solution {
public:
    void solve(vector<vector<char>>& board) {
        for(int i = 0; i < board.size(); ++i) {
            for(int j = 0; j<board[i].size(); ++j) {
                if((i == 0 || i == board.size()-1 || j == 0 || j == board[i].size()-1 && board[i][j] == 'O')) solvedfs(board,i,j);
            }
        }
        for(int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[i].size(); ++j) {
                if(board[i][j] == 'O') board[i][j] = 'X';
                if(board[i][j] == '$') board[i][j] = 'O';
            }
        }
    }
    void solvedfs(vector<vector<char> >& board, int i, int j) {
        if(board[i][j] == 'O') {
            board[i][j] = '$';
            if(i > 0 && board[i-1][j] == 'O') solvedfs(board,i-1,j);
            if(i < board.size()-1 && board[i+1][j] == 'O') solvedfs(board,i+1,j);
            if(j > 0 && board[i][j-1] == 'O') solvedfs(board,i,j-1);
            if(j < board[i].size()-1 && board[i][j+1] == 'O') solvedfs(board,i,j+1);
        }
    }
};
