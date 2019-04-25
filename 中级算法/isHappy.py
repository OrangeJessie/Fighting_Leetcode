# 快乐数
# 编写一个算法来判断一个数是不是“快乐数”。
#
# 一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。
#
# 示例:
#
# 输入: 19
# 输出: true
# 解释:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1


class Solution(object):
    # 当出现的数与之前的重复后，还没有等于1，则不是快乐数
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic = {}
        power = self.calPower(n)
        while power not in dic:
            if power == 1:
                return True
            dic[power] = 1
            power = self.calPower(power)
        return False

    def calPower(self, n):
        power = 0
        while n:
            power += (n%10)**2
            n = n//10
        return power

    # 不是快乐数的数称为不快乐数（unhappy number）
    # 所有不快乐数的数位平方和计算，最後都会进入 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 的循环中。
    def isHappy2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        power = self.calPower(n)
        while True:
            if power == 1:
                return True
            elif power == 89:
                return False
            power = self.calPower(power)
