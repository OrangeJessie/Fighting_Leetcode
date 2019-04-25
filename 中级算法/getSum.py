# 两整数之和
# 不使用运算符 + 和 -，计算两整数a 、b之和。
#
# 示例 1:
#
# 输入: a = 1, b = 2
# 输出: 3


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 把数位限制在32位
        # 只考虑相加的结果，只考虑进位再左移一位的结果，相加
        while b != 0:
            carry = a & b
            a = (a ^ b) % 0x100000000
            b = (carry << 1) % 0x100000000
        return a if a <= 0x7FFFFFFF else a | (~0x100000000+1)
