from collections import Counter


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = Counter(nums)
        for value in dic.values():
            if value >= 2:
                return True
        return False

    def containsDuplicate2(self, nums):
        x = set(nums)
        if len(x) < len(nums):
            return True
        return False


s = Solution()
aa = [1, 3, 3]
print(s.containsDuplicate2(aa))
