class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        b = ""
        length = 2**31
        if len(strs) == 0:
            return ""
        for i in strs:
            le = len(i)
            if le < length:
                length = le
        for j in range(length):
            for i in strs:
                if i[j] != strs[0][j]:
                    return b
            b += strs[0][j]
        return b


s = Solution()
string = []
print(s.longestCommonPrefix(string))
