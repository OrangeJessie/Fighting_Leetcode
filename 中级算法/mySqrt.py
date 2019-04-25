# x 的平方根
# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
#
# 输入: 4
# 输出: 2


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return 0
        left = 1
        right = x
        while left <= right:
            mid = (left+right)//2
            mid_pow = mid**2
            if mid_pow == x:
                return mid
            elif mid_pow > x:
                right = mid - 1
            else:
                if (mid+1)**2 > x:
                    return mid
                left = mid + 1
