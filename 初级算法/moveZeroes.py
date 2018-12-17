class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        counter = 0
        for i in range(l):
            i = i - counter
            if nums[i] == 0:
                counter += 1
                del nums[i]
                num.append(0)


s = Solution()
num = [1, 0, 2, 3, 0, 0, 4]
s.moveZeroes(num)
print(num)
