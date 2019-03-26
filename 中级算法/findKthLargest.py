# 数组中的第K个最大元素
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 示例 1:
#
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return None
        val = [-2147483648]*k
        for i in nums:
            minimum = min(val)
            if i > minimum:
                val[val.index(minimum)] = i
        return min(val)

    # 先归并排序
    def findKthLargest2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return None
        num_sorted = self.sortNums(nums)
        return num_sorted[-k]

    def sortNums(self, nums):
        ln = len(nums)
        if ln <= 1:
            return nums
        mid = ln//2
        num1 = self.sortNums(nums[:mid])
        num2 = self.sortNums(nums[mid:])
        num = self.combine(num1, num2)
        return num

    def combine(self, num1, num2):
        l1 = len(num1)
        l2 = len(num2)
        i = 0
        j = 0
        sort_num = []
        while i < l1 and j < l2:
            if num1[i] < num2[j]:
                sort_num.append(num1[i])
                i += 1
            else:
                sort_num.append(num2[j])
                j += 1
        while i < l1:
            sort_num.append(num1[i])
            i += 1
        while j < l2:
            sort_num.append(num2[j])
            j += 1
        return sort_num
