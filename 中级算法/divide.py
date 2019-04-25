# 两数相除
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
#
# 返回被除数 dividend 除以除数 divisor 得到的商。
#
# 示例 1:
#
# 输入: dividend = 10, divisor = 3
# 输出: 3


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = (dividend > 0)^(divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        val = 0
        while dividend >= divisor:
            step = divisor
            index = 1
            while dividend >= step:
                dividend -= step
                val += index
                index = index<<1
                step = step<<1
        if flag == 1:
            val = -val
        return max(min(val, 2**31-1), -2**31)
