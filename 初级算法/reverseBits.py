class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        if n == 0:
            return 0
        s = ''
        while n > 0:
            s = str(n % 2) + s
            n = n//2
        l = len(s)
        if l < 32:
            d = 32-l
            for i in range(d):
                s = '0' + s
        value = 0
        for i in range(32):
            value += int(s[i])*(2 ** i)
        return value

    def reverseBits2(self, n):
        res = '{0:032b}'.format(n)
        res = res[::-1]
        res = int(res, 2)
        return res
