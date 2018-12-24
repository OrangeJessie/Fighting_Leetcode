class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        b = []
        s = s.lower()
        for i in s:
            if i.isalnum():
                b.append(i)
        l = len(b)//2
        for i in range(l):
            if b[i] != b[-1-i]:
                return False
        return True


s = Solution()
string = "A man, a plan, a canal: Panama"
print(s.isPalindrome(string))
