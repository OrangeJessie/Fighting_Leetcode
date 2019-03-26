# 寻找峰值
# 峰值元素是指其值大于左右相邻值的元素。
#
# 给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
#
# 数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
#
# 你可以假设 nums[-1] = nums[n] = -∞。
#
# 示例 1:
#
# 输入: nums = [1,2,3,1]
# 输出: 2
# 解释: 3 是峰值元素，你的函数应该返回其索引 2。


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        ln = len(nums)
        if ln == 1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return ln-1
        mid = 1
        while mid < ln:
            left = mid - 1
            right = mid + 1
            if right < ln:
                if nums[mid] > nums[right] and nums[mid] > nums[left]:
                    return mid
                elif nums[mid] < nums[right]:
                    mid += 1
                else:
                    mid += 2
        return None
