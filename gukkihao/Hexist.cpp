class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size(),n=board[0].size();
        if (board.empty() || board[0].empty()) return false;
        vector<vector<bool> > visited(m, vector<bool>(n,false));
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(search(board,word,0,i,j,visited)) return true;
            }
        }
        return false;
    }

    bool search(vector<vector<char> > & board,string word,int idx, int i,int j ,vector<vector<bool>>& visited)
    {
        if(idx==word.size()) return true;
        int m=board.size(),n=board[0].size();
        if (i<0 || j<0 || i>=m || j>=n || visited[i][j] || board[i][j]!=word[idx]) return false;
        visited[i][j]=true;
        bool res = search(board,word,idx+1, i-1,j,visited)
                || search(board,word,idx+1, i+1,j,visited)
                || search(board,word,idx+1, i,j-1,visited)
                || search(board,word,idx+1, i,j+1,visited);
        visited[i][j]=false;
        return res;
    }
};
//跟那个计算有几个岛屿的题有点像，主要还是回溯，记录当前搜索位置｀
