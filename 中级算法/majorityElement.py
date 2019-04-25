# 求众数
# 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在众数。
#
# 示例 1:
#
# 输入: [3,2,3]
# 输出: 3


class Solution(object):
    def majorityElement(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            # 排序后处在中间的一定是众数
            nums.sort()
            return nums[len(nums)/2]

    # 我的做法
    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ln = len(nums)//2
        if not nums:
            return None
        dictionary = {}
        for i in nums:
            try:
                dictionary[i] += 1
            except:
                dictionary[i] = 1
        for i in dictionary.keys():
            if dictionary[i] > ln:
                return i
        return None
