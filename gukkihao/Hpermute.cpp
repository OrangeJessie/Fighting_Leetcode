class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int> >ans;
        vector<int> visited(nums.size(),0);
        vector<int> temp;
        permute(nums,0,temp,visited,ans);
        return ans;
    }
    void permute(const vector<int>&nums, int level, vector<int> &temp,vector<int>visited,vector<vector<int> > &ans)
    {
        if(level == nums.size())  ans.push_back(temp);
        else
        {
            for (int i= 0;i<nums.size();i++)
            {
                if(visited[i]==0) 
                {
                    visited[i]=1;
                    temp.push_back(nums[i]);
                    permute(nums,level+1,temp,visited,ans);
                    temp.pop_back();
                    visited[i]=0;
                }
                
            }
        }
        
    }
};
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        int start=0;
        vector<vector<int> > ans;
        permute(nums,start,ans);
        return ans;
    }
    void permute(vector<int>&nums, int start, vector<vector<int> >& ans)
    {
        if(start>=nums.size()) ans.push_back(nums);
        for(int i=start;i<nums.size();i++)
        {
            swap(nums[start],nums[i]);
            permute(nums,start+1,ans);
            swap(nums[start],nums[i]);
        }
    }
};
