class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1 = {}
        d2 = {}
        for i in nums1:
            if d1.get(i):
                d1[i] += 1
            else:
                d1[i] = 1
        for i in nums2:
            if d2.get(i):
                d2[i] += 1
            else:
                d2[i] = 1
        a = []
        for i in d1.keys():
            if d2.get(i):
                num = min(d1[i], d2[i])
                for i2 in range(num):
                    a.append(i)
        return a

    def intersect2(self, nums1, nums2):
        res = []
        for i in nums1:
            if i in nums2:
                res.append(i)
                nums2.remove(i)
        return res


s = Solution()
nums1 = [1, 2, 3, 4, 4]
nums2 = [1, 3, 4, 4, 4]
print(s.intersect(nums1, nums2))
