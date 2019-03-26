# 跳跃游戏
# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个位置。
#
# 示例 1:
#
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        nums = nums[::-1]
        ln = len(nums)
        if ln <= 1:
            return True
        # 边界条件
        if nums[1] > 0:
            can = [1, 1]
        else:
            can = [1, 0]
        # 开始转移方程
        for i in range(2, ln):
            if 1 not in can[max(i-nums[i], 0):i]:
                can.append(0)
                continue
            subcan = 0
            jump = min(nums[i], i)
            while jump > 0:
                subcan = can[i-jump]
                jump -= 1
                if subcan:
                    break
            if subcan:
                can.append(1)
            else:
                can.append(0)
        return bool(can[-1])

    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mingood = len(nums) - 1                 # 数组最大的下标
        for i in range(len(nums)-2, -1, -1):    # 当数组值与下标之和大于最大下标，则可以从当前值到最后
            if i + nums[i] >= mingood:          # 从倒数第二位开始判断能不能到最后一位，如果能，将数组缩短，最大下标减小为当前下标
                mingood = i

        return mingood == 0                     # 判断下标为0，即第一个能否到达最后
