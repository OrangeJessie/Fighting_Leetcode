# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
#
# 注意:
# 不能使用代码库中的排序函数来解决这道题。
#
# 示例:
#
# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
# 进阶：
#
# 一个直观的解决方案是使用计数排序的两趟扫描算法。
# 首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
# 你能想出一个仅使用常数空间的一趟扫描算法吗？


class Solution(object):
    # 两趟扫描
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        red = 0
        white = 0
        blue = 0
        index = 0
        for item in nums:
            if item == 0:
                red += 1
            elif item == 1:
                white += 1
            else:
                blue += 1
        while red > 0:
            nums[index] = 0
            index += 1
            red -= 1
        while white > 0:
            nums[index] = 1
            index += 1
            white -= 1
        while blue > 0:
            nums[index] = 2
            index += 1
            blue -= 1

    def sortColors2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums:
            ln = len(nums)
            left = 0
            right = ln-1
            find = 0
            while find <= right and left < right:
                if nums[find] == 1:
                    find += 1
                elif nums[find] == 0:
                    nums[find] = nums[left]             # left的要么是1要么是0，所以不需要再判断交换之后的find
                    nums[left] = 0
                    left += 1
                    find += 1
                elif nums[find] == 2:
                    nums[find] = nums[right]            # right的数据不确定，还需要再判断交换之后的find
                    nums[right] = 2
                    right -= 1
