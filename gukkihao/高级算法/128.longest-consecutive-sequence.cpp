/*
 * @lc app=leetcode id=128 lang=cpp
 *
 * [128] Longest Consecutive Sequence
 *
 * https://leetcode.com/problems/longest-consecutive-sequence/description/
 *
 * algorithms
 * Hard (41.36%)
 * Total Accepted:    200.7K
 * Total Submissions: 485.1K
 * Testcase Example:  '[100,4,200,1,3,2]'
 *
 * Given an unsorted array of integers, find the length of the longest
 * consecutive elements sequence.
 * 
 * Your algorithm should run in O(n) complexity.
 * 
 * Example:
 * 
 * 
 * Input: [100, 4, 200, 1, 3, 2]
 * Output: 4
 * Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
 * Therefore its length is 4.
 * 
 * 
 */
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.empty()) return 0;
        unordered_set<int>s(nums.begin(),nums.end());
        int ans=0;
        for(int num : nums) {
            if(!s.count(num)) continue;
            s.erase(num);
            int pre=num-1,next=num+1;
            while(s.count(pre)) s.erase(pre--);
            while(s.count(next)) s.erase(next++);
            ans=max(ans,next-pre-1);
        }
        return ans;

        
    }
};

