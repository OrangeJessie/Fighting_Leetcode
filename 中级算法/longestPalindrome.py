# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。


class Solution(object):
    # 回文有两种情况，一种是初始奇数回文一种是初始偶数回文，以候选最大回文字符串的倒数第二位为中心点i
    # 奇数回文的边界为：i+1，i-maxlen-1，偶数回文的边界为：i+1, i-maxlen
    # 奇数的前边界在偶数的前面一位，判断为偶数回文后，下一次偶数回文判断的start不变，判断为奇数回文后，下一次start提前一位
    # 判断框只能增大，start永远是最大判断框的开始
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) < 2 or s == s[::-1]:
            return s
        n = len(s)
        start, maxlen = 0, 1

        for i in range(1, n):

            odd = s[i - maxlen - 1:i + 1]
            even = s[i - maxlen:i + 1]

            if i - maxlen - 1 >= 0 and odd == odd[::-1]:
                start = i - maxlen - 1
                maxlen += 2
                continue
            if i - maxlen >= 0 and even == even[::-1]:
                start = i - maxlen
                maxlen += 1

        return s[start:start + maxlen]

    # 找回文子串中心点
    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls = len(s)
        if ls <= 1:
            return s
        if ls == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        index = []
        m = 1
        a = 0
        b = 1
        for i in range(1, ls-1):
            if s[i-1] == s[i+1]:
                index.append(i)
        for i in index:
            before = i-1
            last = i+1
            while before >= 0 and last <= ls-1:
                if s[before] != s[last]:
                    break
                else:
                    before -= 1
                    last += 1
            before += 1
            last -= 1
            temp = last - before + 1
            if temp > m:
                        m = temp
                        a = before
                        b = last+1
        index2 = []
        for i in range(0, ls-1):
            if s[i] == s[i+1]:
                index2.append(i)
        for i in index2:
            before = i
            last = i+1
            while before >= 0 and last <= ls-1:
                if s[before] != s[last]:
                    break
                else:
                    before -= 1
                    last += 1
            before += 1
            last -= 1
            temp = last - before + 1
            if temp > m:
                m = temp
                a = before
                b = last+1
        return s[a:b]



    # 超出时间限制了
    def longestPalindrome3(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        ls = len(s)
        m = 1
        a = 0
        b = 1
        for i in range(ls):
            j = i
            while j < ls:
                if s[j] != s[i]:
                    j += 1
                else:
                    r = self.isPalindrome(s[i:j+1])
                    if r & (j+1-i > m):
                        m = j+1-i
                        a = i
                        b = j+1
                    j += 1
        return s[a:b]

    def isPalindrome(self, ss):
        before = 0
        last = len(ss)-1
        while before <= last:
            if ss[before] != ss[last]:
                return False
            before += 1
            last -= 1
        return True


s = Solution()
print(s.longestPalindrome('abacabba'))
