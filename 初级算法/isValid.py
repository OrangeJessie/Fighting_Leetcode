class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s.replace(' ', '')
        # l = len(s)
        # odd = l % 2
        match = {'(': ')', '[': ']', '{': '}'}
        # if odd:
        #     return False
        un_match = []
        for i in s:
            if un_match:
                u = un_match[-1]
                if u not in match.keys():
                    return False
                if match[u] == i:
                    un_match = un_match[0:-1]
                else:
                    un_match.append(i)
            else:
                un_match.append(i)
        if un_match == []:
            return True
        return False

    # 如果是')', ']', '}'中的任意一个则判断是否与前面匹配
    def isValid2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                d = stack.pop() if stack else '#'
                if mapping[char] != d:
                    return False
            else:
                stack.append(char)
        return not stack
