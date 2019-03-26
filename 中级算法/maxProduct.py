# 乘积最大子序列
# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
#
# 示例 1:
#
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnum = 1
        minnum = 1
        ln = len(nums)
        total_max = -2147483648
        for i in range(ln):
            if nums[i] < 0:
                temp = maxnum
                maxnum = minnum
                minnum = temp
            maxnum = max(nums[i], maxnum*nums[i])       # 解决当前是0的问题
            minnum = min(nums[i], minnum*nums[i])
            if maxnum > total_max:
                total_max = maxnum
        return total_max

    def maxProduct2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(max(A), max(B))
