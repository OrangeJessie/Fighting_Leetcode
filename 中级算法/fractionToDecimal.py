# 分数到小数
# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。
#
# 如果小数部分为循环小数，则将循环的部分括在括号内。
#
# 示例 1:
#
# 输入: numerator = 1, denominator = 2
# 输出: "0.5"


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # 这个题首先要考虑正负号的情况
        # 判断是否循环要用 不断地乘10倍取余 的方法，当余数出现重复时，从重复的数字第一次出现的地方开始循环
        if numerator == 0:
            return '0'
        flag = (int(numerator < 0))^(int(denominator < 0))
        numerator = abs(numerator)
        denominator = abs(denominator)
        if numerator % denominator == 0:
            if flag == 1:
                return '-' + str(numerator//denominator)
            else:
                return str(numerator//denominator)
        val = []
        int_val = []
        int_val.append(str(numerator//denominator))
        int_val.append('.')
        numerator = numerator%denominator
        res = []
        begin = -1
        end = -1
        while numerator:
            if numerator not in res:
                res.append(numerator)
            else:
                begin = res.index(numerator)
                end = len(res)-1
                break
            val.append(str(numerator*10//denominator))
            numerator = numerator * 10 % denominator
        if flag == 1:
            if begin == -1 and end == -1:
                return '-'+''.join(int_val + val)
            return '-'+''.join(int_val + val[:begin] + ['('] + val[begin:] + [')'])
        else:
            if begin == -1 and end == -1:
                return ''.join(int_val + val)
            return ''.join(int_val + val[:begin] + ['('] + val[begin:] + [')'])
