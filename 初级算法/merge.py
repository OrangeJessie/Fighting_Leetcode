class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
        i = 0
        j = 0
        k = 0
        nums3 = nums1[:m]
        while i < m and j < n:
            if nums3[i] > nums2[j]:
                nums1[k] = nums2[j]
                j += 1
            elif nums3[i] <= nums2[j]:
                nums1[k] = nums3[i]
                i += 1
            k += 1
        if i >= m:
            nums1[k:] = nums2[j:]
        elif i < m:
            nums1[k:] = nums3[i:]


