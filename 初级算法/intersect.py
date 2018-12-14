class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        x1 = Counter(nums1)
        x2 = Counter(nums2)
        a = []
        for i in x1.keys():
            if x2[i] != 0:
                num = min(x1[i], x2[i])
                for i2 in range(num):
                    a.append(i)
        return a


s = Solution()
nums1 = [1, 2, 3, 4, 4]
nums2 = [1, 3, 4, 4, 4]
print(s.intersect(nums1, nums2))
