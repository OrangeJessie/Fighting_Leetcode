/*
设置标志位，假设第一位数字是众数，依次向后确认，如果是,加一，不过不是，减一，标志位减到0的时候移位
*/
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int ans=0,cnt=0;
        for(auto num:nums)
        {
            if(cnt==0) {ans=num;++cnt;}
            else(num==ans) ? ++cnt : --cnt;
        }
        return ans;
    }
};
