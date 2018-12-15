class Solution:
    # 还可以存为字典
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        diff = []
        for i in range(l):
            diff.append(target-nums[i])
        tar = list(set(nums).intersection(diff))
        b = []
        for i in tar:
            a = nums.count(i)
            if a == 2:
                b = [i2 for (i2, z) in enumerate(nums) if z == i]
            elif i != target/2:
                b.append(nums.index(i))
        return b


s = Solution()
num = [3, 2, 4]
t = 6
print(s.twoSum(num, t))
