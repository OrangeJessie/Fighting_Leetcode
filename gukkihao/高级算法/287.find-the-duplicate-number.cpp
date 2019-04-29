/*
 * @lc app=leetcode id=287 lang=cpp
 *
 * [287] Find the Duplicate Number
 *
 * https://leetcode.com/problems/find-the-duplicate-number/description/
 *
 * algorithms
 * Medium (49.11%)
 * Total Accepted:    180.3K
 * Total Submissions: 367.1K
 * Testcase Example:  '[1,3,4,2,2]'
 *
 * Given an array nums containing n + 1 integers where each integer is between
 * 1 and n (inclusive), prove that at least one duplicate number must exist.
 * Assume that there is only one duplicate number, find the duplicate one.
 * 
 * Example 1:
 * 
 * 
 * Input: [1,3,4,2,2]
 * Output: 2
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [3,1,3,4,2]
 * Output: 3
 * 
 * Note:
 * 
 * 
 * You must not modify the array (assume the array is read only).
 * You must use only constant, O(1) extra space.
 * Your runtime complexity should be less than O(n^2).
 * There is only one duplicate number in the array, but it could be repeated
 * more than once.
 * 
 * 
 */
/*class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        if(nums.empty()) return 0;
        int left=0,right=nums.size()-1;
        while(left<right) {
            int mid = left + (right - left) / 2, cnt = 0;
            for(num : nums) {
                if(num<mid) ++cnt;
            }
            if(cnt<=mid) left=mid+1;
            else right=mid;

        }
        return right;
        
    }
};*/
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        if(nums.empty())  return 0;
        int slow = 0,fast = 0, ans =0;
        while(true) {
            slow=nums[slow];
            fast = nums[nums[fast]];
            if(fast==slow) break;
        }
        while(true) {
            slow=nums[slow];
            ans=nums[ans];
            if(slow==ans) break;
        }
        return ans;
    }
};
