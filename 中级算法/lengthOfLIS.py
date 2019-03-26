# Longest Increasing Subsequence
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 示例:
#
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 说明:
#
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n2) 。
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?


class Solution(object):
    # 贪心算法+二分
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tail = []
        for num in nums:                    # 贪心算法，时间复杂度O（n）
            if not tail or num > tail[-1]:
                tail.append(num)
            elif num in tail:
                continue
            else:                           # 每个数字是否更新，使用二分法，时间复杂度O（lgn），所以总的时间复杂度为O（nlgn）
                left = 0
                right = len(tail)-1
                while left < right:
                    mid = (left+right)//2
                    if tail[mid] > num:
                        right = mid
                    else:
                        left = mid+1
                tail[left] = num
        return len(tail)

    # 动态规划
    def lengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ln = len(nums)
        dp = [1]*ln
        for i in range(1, ln):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
