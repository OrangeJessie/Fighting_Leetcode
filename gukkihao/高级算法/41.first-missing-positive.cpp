/*
 * @lc app=leetcode id=41 lang=cpp
 *
 * [41] First Missing Positive
 *
 * https://leetcode.com/problems/first-missing-positive/description/
 *
 * algorithms
 * Hard (28.58%)
 * Total Accepted:    203.6K
 * Total Submissions: 712.2K
 * Testcase Example:  '[1,2,0]'
 *
 * Given an unsorted integer array, find the smallest missing聽positive
 * integer.
 * 
 * Example 1:
 * 
 * 
 * Input: [1,2,0]
 * Output: 3
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [3,4,-1,1]
 * Output: 2
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: [7,8,9,11,12]
 * Output: 1
 * 
 * 
 * Note:
 * 
 * Your algorithm should run in O(n) time and uses constant extra space.
 * 
 */
/*class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        if(nums.empty()) return 1;
        unordered_set<int>s;
        int mx=0;
        for(int num:nums){
            if(num<=0) continue;
            s.insert(num);
            mx=max(mx,num);
        }
        for(int i=1;i<=mx;i++){
            if(!s.count(i)) return i;
        }
        return mx+1;
        
    }
};*/
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        if(nums.empty()) return 1;
        int n=nums.size();
        for(int i=0;i<n;++i) {
            while(nums[i]>0&&nums[i]<= n && nums[i]!=nums[nums[i]-1]) {
                swap(nums[i],nums[nums[i]-1]);
            }   
        }
        for(int i = 0;i < n;++i) {
            if(nums[i] != i + 1)
                return i + 1;
        }
        return n + 1;
    }
};

