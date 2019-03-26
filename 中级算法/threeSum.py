# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution(object):
    # 时间复杂度很高
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        t = []
        p = []
        for i in range(n):
            if nums[i] in p:
                continue
            else:
                p.append(nums[i])
            target = - nums[i]
            sub = self.twoSum(nums[i+1:], target)
            if not sub:
                continue
            for o in sub:
                o = o + [nums[i]]
                for i3 in range(2):
                    for i2 in range(2):
                        if o[i2] > o[i2+1]:
                            temp = o[i2]
                            o[i2] = o[i2+1]
                            o[i2+1] = temp
                if o not in t:
                    t.append(o)
        return t

    def twoSum(self, nums, target):
        sub = []
        b = {}
        for i in nums:
            a = target - i
            if i in b:
                if [i, a] not in sub:
                    sub.append([i, a])
            else:
                b[a] = i
        return sub

    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num_dict = {}
        result = []

        for i in nums:
            if i in num_dict:
                num_dict[i] += 1
            else:
                num_dict[i] = 1

        pos = [i for i in num_dict if i > 0]
        neg = [i for i in num_dict if i < 0]
        neg.sort()

        if 0 in num_dict and num_dict[0] >= 3:
            result.append([0, 0, 0])
        for i in pos:
            for j in neg:
                k = -i-j
                if k in num_dict:
                    if (k == i or k == j) and num_dict[k] >= 2:
                        result.append([i, k, j])
                    elif j < k < i:
                        result.append([i, k, j])
                    if k < j:
                        break
        return result
