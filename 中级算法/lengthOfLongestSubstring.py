# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。


class Solution(object):
    # 从第一个开始，计算出每一个为开头最长的子串
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        m = 1
        ls = len(s)
        for i in range(ls):
            j = i
            d = []
            while j < ls:
                if s[j] in d:
                    break
                else:
                    d.append(s[j])
                    j += 1
            temp = j-i              # 最后一个如果是相同的，j已经加了1，所以后面减的时候j不能再加1
            if temp > m:
                m = temp
        return m

    # 在不遇到重复符号的时候，start不改变，为候选最长序列开始的位置，当遇到重复符号后，start改变到第二个重复符号+1的位置
    # 字典中存的是最近的某符号的位置，用于判断是否重复
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        start = 0
        length = len(s)
        dic = {}
        for i in range(length):
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                if dic[s[i]]+1 > start:
                    start = dic[s[i]] + 1
                dic[s[i]] = i
            if l < i-start+1:
                l = i - start + 1
        return l

