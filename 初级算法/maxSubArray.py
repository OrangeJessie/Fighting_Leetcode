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

    # 分治算法：最大子数组要么在左边要么在右边，要么横跨在中间，在左右两边时是递归问题，最终最大子数组一定会横跨一个中间。
    # 容易出错的地方：横跨中间的子程序标号，python中以0开始，用//求到mid后，数组为偶数mid偏后，因此计算时把mid划分到右边。
    def maxSubArray2(self, nums):
        l = len(nums)
        if l <= 1:
            return nums[0]
        mid = l//2
        low = 0
        high = l-1
        max_mid = self.maxAcrossMid(nums, low, high, mid)
        max_left = self.maxSubArray2(nums[:mid+1])
        max_right = self.maxSubArray2(nums[mid+1:])
        real_max = max(max_mid, max_left)
        real_max = max(real_max, max_right)
        return real_max

    def maxAcrossMid(self, nums, low, high, mid):
        left_sum = -2**32
        right_sum = -2**32
        sum = 0
        for i in range(mid-1, low-1, -1):
            sum += nums[i]
            if sum > left_sum:
                left_sum = sum
        sum = 0
        for i in range(mid, high+1):
            sum += nums[i]
            if sum > right_sum:
                right_sum = sum
        max_sum = left_sum + right_sum
        return max_sum


s = Solution()
nums = [8,-19,5,-4,20]
s.maxSubArray2(nums)
