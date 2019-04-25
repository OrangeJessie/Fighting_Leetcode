# 逆波兰表达式求值
# 根据逆波兰表示法，求表达式的值。
#
# 有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
#
# 说明：
#
# 整数除法只保留整数部分。
# 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
# 示例 1：
#
# 输入: ["2", "1", "+", "3", "*"]
# 输出: 9
# 解释: ((2 + 1) * 3) = 9


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0
        dictionary = {'+': 1, '-': 1, '*': 1, '/': 1}
        stack = []
        for i in tokens:
            if i in dictionary:
                val1 = stack.pop()
                val2 = stack.pop()
                if i == '+':
                    stack.append(val1+val2)
                elif i == '-':
                    stack.append(val2-val1)
                elif i == '*':
                    stack.append(val2*val1)
                else:
                    stack.append(int(float(val2)/float(val1)))
            else:
                stack.append(int(i))
        return stack.pop()
