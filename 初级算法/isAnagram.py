class Solution:
    # 速度较慢
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        b1 = {}
        b2 = {}
        for i in s:
            if i not in b1:
                b1[i] = 1
            else:
                b1[i] += 1
        for i in t:
            if i not in b2:
                b2[i] = 1
            else:
                b2[i] += 1
        if b1 == b2:
            return True
        else:
            return False

    # 速度稍有提升
    def isAnagram2(self, s, t):
        b1 = {}
        for i in s:
            if i not in b1:
                b1[i] = 1
            else:
                b1[i] += 1
        for i in t:
            if i not in b1:
                return False
            else:
                b1[i] -= 1
                if b1[i] < 0:
                    return False
        if sum(b1.values()) > 0:
            return False
        else:
            return True

    # 速度又有提升
    def isAnagram3(self, s, t):
        if len(t) != len(s):
            return False
        c = set(t)
        for i in c:
            if t.count(i) != s.count(i):
                return False
        return True


s = Solution()
s1 = 'ab'
s2 = 'ab'
print(s.isAnagram3(s1, s2))
