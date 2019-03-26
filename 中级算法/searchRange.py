# 在排序数组中查找元素的第一个和最后一个位置
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 如果数组中不存在目标值，返回 [-1, -1]。
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        ln = len(nums)
        left = 0
        right = ln-1
        val = []
        while right - left >= 0:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                val.append(mid)
                left = mid-1
                right = mid+1
                while left >= 0:
                    if nums[left] == target:
                        val.append(left)
                        left -= 1
                    else:
                        break
                while right <= ln-1:
                    if nums[right] == target:
                        val.append(right)
                        right += 1
                    else:
                        break
                break
            else:
                left = mid + 1
        lv = len(val)
        if lv == 0:
            val = [-1, -1]
        return [min(val), max(val)]
