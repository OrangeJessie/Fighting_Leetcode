class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        b = []
        b_s = ''
        l = len(s)
        r_l = int(l/2)
        for i in s:
            b.append(i)
        for i in range(r_l):
            a = b[i]
            b[i] = b[l-1-i]
            b[l-1-i] = a
        for i in b:
            b_s = b_s + i
        return b_s


sol = Solution()
string = 'hello'
print(sol.reverseString(string))
