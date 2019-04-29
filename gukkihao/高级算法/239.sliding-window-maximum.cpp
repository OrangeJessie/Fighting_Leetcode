/*
 * @lc app=leetcode id=239 lang=cpp
 *
 * [239] Sliding Window Maximum
 *
 * https://leetcode.com/problems/sliding-window-maximum/description/
 *
 * algorithms
 * Hard (37.75%)
 * Total Accepted:    150.9K
 * Total Submissions: 399.6K
 * Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
 *
 * Given an array nums, there is a sliding window of size k which is moving
 * from the very left of the array to the very right. You can only see the k
 * numbers in the window. Each time the sliding window moves right by one
 * position. Return the max sliding window.
 * 
 * Example:
 * 
 * 
 * Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
 * Output: [3,3,5,5,6,7] 
 * Explanation: 
 * 
 * Window position                Max
 * ---------------               -----
 * [1  3  -1] -3  5  3  6  7       3
 * ‚Å?1 [3  -1  -3] 5  3  6  7       3
 * ‚Å?1  3 [-1  -3  5] 3  6  7       5
 * ‚Å?1  3  -1 [-3  5  3] 6  7       5
 * ‚Å?1  3  -1  -3 [5  3  6] 7       6
 * ‚Å?1  3  -1  -3  5 [3  6  7]      7
 * 
 * 
 * Note: 
 * You may assume k is always valid, 1 ‚â? k ‚â? input array's size for non-empty
 * array.
 * 
 * Follow up:
 * Could you solve it in linear time?
 */
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int>q;
        vector<int>ans;
        for(int i = 0; i < nums.size(); ++i) {
            if(!q.empty() && q.front() == i-k ) q.pop_front();
            while(!q.empty()&&nums[q.back()]<nums[i]) q.pop_back();
            q.push_back(i);
            if(i>=k-1) ans.push_back(nums[q.front()]);
        }
        return ans;  
    }
};
