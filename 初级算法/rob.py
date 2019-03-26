class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        elif l == 1:
            return nums[0]
        else:
            money = [0] * l
            money[0], money[1] = nums[0], max(nums[0], nums[1])
            for i in range(2, l):
                money[i] = max(nums[i]+money[i-2], money[i-1])
            return money[l-1]
