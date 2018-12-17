from collections import Counter


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        diction = {}
        for i in nums:
            if i not in diction:
                diction[i] = 1
            else:
                return True
        return False


s = Solution()
aa = [1, 3, 3]
print(s.containsDuplicate2(aa))
