class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        l1 = len(needle)
        l2 = len(haystack)
        for i in range(l2-l1+1):
            if needle[0] == haystack[i]:
                if needle == haystack[i:i+l1]:
                    return i
        return -1


s = Solution()
hay = "a"
need = ""
print(s.strStr(hay, need))
