class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        b = {}
        for i in s:
            if i not in b:
                b[i] = 1
            else:
                b[i] += 1
        if 1 in b.values():
            x = list(b.keys())[list(b.values()).index(1)]
            return s.index(x)
        else:
            return -1

    def firstUniqChar2(self, s):
        b = {}
        for i in s:
            if i not in b:
                b[i] = 1
            else:
                b[i] += 1
        for i in b.keys():
            if b[i] == 1:
                return s.index(i)
        return -1


s = Solution()
string = 'loveyoulovp'
print(s.firstUniqChar(string))
