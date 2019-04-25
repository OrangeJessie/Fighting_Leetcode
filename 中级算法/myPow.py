# Pow(x, n)
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
#
# 示例 1:
#
# 输入: 2.00000, 10
# 输出: 1024.00000


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not x:
            return 0
        if not n:
            return 1
        if n < 0:
            flag = 1
            n = -n
        else:
            flag = 0
        pow_val = 1
        while n > 0:
            if n & 1:
                pow_val = pow_val * x
            x = x*x
            n /= 2
        if flag == 0:
            return pow_val
        return 1/pow_val
