# 前K个高频元素
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
#
# 示例 1:
#
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        val = [0]*k
        val_index = [0]*k
        for i in d:
            if d[i] > min(val):
                index = val.index(min(val))
                val[index] = d[i]
                val_index[index] = i
        return val_index
