class Solution:
    # 空间复杂度高
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        b = []
        l = len(x)-1
        for i in x:
            b.append(i)
        if b[0] == '-':
            b_s = '-'
            for i2 in range(l, 0, -1):
                b_s = b_s + b[i2]
        else:
            b_s = ''
            for i2 in range(l, -1, -1):
                b_s = b_s + b[i2]
        b_s = int(b_s)
        if b_s < -2**31 or b_s > 2**31-1:
            return 0
        else:
            return b_s

    def reverse2(self, x):
        rev = 0
        max_valid = int((2**31-1)/10)
        min_valid = int(-2**31/10)
        if x < 0:
            a = -1
        else:
            a = 1
        x = abs(x)
        while x != 0:
            pop = x % 10
            x = x//10
            if rev > max_valid | (rev == max_valid & pop > 7):
                return 0
            elif rev < min_valid | (rev == min_valid | pop < -8):
                return 0
            temp = rev * 10 + pop
            rev = temp
        return a*rev


s = Solution()
x = -123
print(s.reverse2(x))
