import time


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        for i in range(0, len(nums)-1):
            if nums[i] != nums[i+1]:
                count = count + 1
        p = 0
        while p < count and p < len(nums)-1:
            if nums[p] == nums[p+1]:
                del nums[p+1]
            else:
                p += 1
        return len(nums)


s = Solution()
num = [1, 1, 2, 3, 3, 4, 5]
# start_time = time.time()
length = s.removeDuplicates(num)
# end_time = time.time()
print(num)

