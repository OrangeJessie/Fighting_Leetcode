class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        x = Counter(nums)
        return list(x.keys())[list(x.values()).index(1)]

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        x = Counter(nums)
        for i in x:
            print(x[i])
            if x[i] == 1:
                return i


s = Solution()
num = [1, 1, 4, 3, 3]
print(s.singleNumber(num))
