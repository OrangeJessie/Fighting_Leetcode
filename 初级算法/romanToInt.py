class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        num = 0
        length = len(s)
        i = 0
        while i < length-1:
            if s[i] == 'M':
                num += 1000
            elif s[i] == 'D':
                num += 500
            elif s[i] == 'C':
                if s[i+1] == 'M':
                    num += 900
                    i += 1
                elif s[i+1] == 'D':
                    num += 400
                    i += 1
                else:
                    num += 100
            elif s[i] == 'L':
                num += 50
            elif s[i] == 'X':
                if s[i+1] == 'C':
                    num += 90
                    i += 1
                elif s[i+1] == 'L':
                    num += 40
                    i += 1
                else:
                    num += 10
            elif s[i] == 'V':
                num += 5
            elif s[i] == 'I':
                if s[i+1] == 'X':
                    num += 9
                    i += 1
                elif s[i+1] == 'V':
                    num += 4
                    i += 1
                else:
                    num += 1
            i += 1
        if i == length-1:
            if s[length-1] == 'M':
                num += 1000
            elif s[length-1] == 'D':
                num += 500
            elif s[length-1] == 'C':
                num += 100
            elif s[length-1] == 'L':
                num += 50
            elif s[length-1] == 'X':
                num += 10
            elif s[length-1] == 'V':
                num += 5
            elif s[length-1] == 'I':
                num += 1
        return num

    def romanToInt2(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        for i in range(len(s)):
            if i<len(s)-1 and map[s[i]]<map[s[i+1]]:
                ans -= map[s[i]]
            else:
                ans += map[s[i]]
        return ans
