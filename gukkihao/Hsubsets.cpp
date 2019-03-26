class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int> > ans;
        vector<int> temp;
        int level=0;
        subsets(nums,level, temp,ans);
        return ans;
    }
    void subsets(vector<int> nums, int level, vector<int>& out, vector<vector<int> >&ans)
    {
        ans.push_back(out);
        for(int i=level;i<nums.size();i++)
        {
            out.push_back(nums[i]);
            subsets(nums,i+1,out,ans);
            out.pop_back();//为什么
        }
    }
};
//回溯算法，形式都差不多的，
