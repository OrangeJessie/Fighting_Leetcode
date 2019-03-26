//rob和notrob表示偷或者不偷当前房子小偷获得的最大利润
class Solution {
public:
    int rob(vector<int>& nums) {
        int rob=0,Notrob=0;
        for(int i=0;i<nums.size();i++)
        {
            int prerob=rob; int preNotrob=Notrob;
            rob=nums[i]+preNotrob;
            Notrob=max(prerob,preNotrob);
        }
        return max(rob,Notrob);
    }
};
//状态转移公式
class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size()<=1) return nums.empty()?0:nums[0];
        vector<int> ans;
        ans.push_back(nums[0]);
        ans.push_back(max(nums[0],nums[1]));
        for(int i=2;i<nums.size();i++)
        {
            ans.push_back(max(ans[i-1],nums[i]+ans[i-2]));
        }
        return ans.back();

    }
};
