//计数排序，先数一下0,1,2 各有多少个，然后分别存进去，再依次写进原数组
/*
class Solution {
public:
    void sortColors(vector<int>& nums) {
        vector<int> temp(3,0);
        int idx=0;
        for(int i=0;i<nums.size();i++)
        {
            temp[nums[i]]++;
        }
        nums.clear();
        for(int i=0;i<temp.size();i++)
        {
            for(int j=0;j<temp[i];j++)
            {
                nums.push_back(i);
            }
            
        }
    }
};
*/
class Solution {
public:
        void sortColors(vector<int>& nums) {
        int left=0,right=nums.size()-1;
        for(int i=0;i<=right;i++)
        {
            if(nums[i]==0)
                swap(nums[i],nums[left++]);
            else if(nums[i]==2)
                swap(nums[i--],nums[right--]);
        }
    }
    
};
