class Solution:
    # 还可以存为字典
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        # 创建一个空字典
        d = {}
        for x in range(n):
            a = target - nums[x]
            # 字典d中存在nums[x]时
            if nums[x] in d:
                return [d[nums[x]], x]
            # 否则往字典增加键/值对
            else:
                d[a] = x


s = Solution()
num = [3, 2, 4]
t = 6
print(s.twoSum(num, t))
