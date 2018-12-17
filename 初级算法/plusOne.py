class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] < 9:
            digits[-1] = digits[-1] + 1
            return digits
        elif len(digits) > 1:
            digits[-1] = 0
            digits[0:-1] = self.plusOne(digits[0:-1])
        else:
            digits[-1] = 0
            digits.append(1)
            l = len(digits)
            for i in range(l):
                digits[l-1-i] = digits[l-2-i]
            digits[0] = 1
        return digits

    def plusOne2(self, digits):
        num = 0
        l = len(digits)
        for (index, i) in enumerate(digits):
            num = num + i*10**(l-index-1)
        num = num + 1
        num = str(num)
        new = []
        for i in num:
            new.append(int(i))
        return new

    # 速度是最快的
    def plusOne3(self, digits):
        if digits[-1] < 9:
            digits[-1] = digits[-1] + 1
            return digits
        elif len(digits) > 1:
            digits[-1] = 0
            digits[0:-1] = self.plusOne(digits[0:-1])
        else:
            digits[-1] = 0
            digits.reverse()
            digits.append(1)
            digits.reverse()
        return digits


s = Solution()
digit = [9]
print(s.plusOne3(digit))
