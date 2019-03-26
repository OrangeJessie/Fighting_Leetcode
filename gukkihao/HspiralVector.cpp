/*顺时针读取二维数组，分别定力数组的四个边界，然后进行读取*/
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if(matrix.empty()||matrix[0].empty()) return {};
        int m=matrix.size(),n=matrix[0].size();
        int up=0,down=m-1,left=0,right=n-1;
        vector<int>ans;
        while(true)
        {
            for(int j=left;j<=right;++j) ans.push_back(matrix[up][j]);
            if(++up>down) break;
            for(int i=up;i<=down;++i) ans.push_back(matrix[i][right]);
            if(--right<left) break;
            for(int j=right;j>=left;--j) ans.push_back(matrix[down][j]);
            if(--down<up) break;
            for(int i=down;i>=up;--i) ans.push_back(matrix[i][left]);
            if(++left>right) break;
        }
        return ans;
        
    }
};


