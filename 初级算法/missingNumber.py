class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        nums.append(-1)
        for i in range(l):
            temp = nums[nums[i]]
            nums[nums[i]] = nums[i]
            nums[i] = temp
        s = []
        v = []
        for i in range(l+1):
            if nums[i] != i:
                s.append(i)
                v.append(nums[i])
        for i in s:
            if i not in v:
                return i

    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_max = max(nums)
        nums_len = len(nums)
        if temp_max != nums_len:
            return nums_len
        return (temp_max+1) * temp_max/2 - sum(nums)

    def missingNumber3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums)+1)) - sum(nums)
