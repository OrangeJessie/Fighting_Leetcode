# 全排列
# 给定一个没有重复数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, num, sub, res):
        if not num:
            res.append(sub)
        else:
            ln = len(num)
            for i in range(ln):
                self.dfs(num[:i]+num[i+1:], sub+[num[i]], res)
