class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        max_sub_sum = nums[0]
        for num in nums:
            sum += num
            if sum > max_sub_sum:
                max_sub_sum = sum
            if sum < 0:                 # 如果数组的前面是负的，那么新的子数组从非负的地方开始
                sum = 0
        return max_sub_sum
