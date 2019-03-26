class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str == '':
            return 0
        i = 0
        l = len(str)
        count = 0
        while str[i] == ' ':            # 删除字符串前缀 strip()
            count += 1
            i += 1
            if i > l-1:
                return 0
        j = i-int(count != 0)
        if (str[i] == '-') | (str[i] == '+'):
            i = i+1
        elif not str[i].isdigit():
            return 0
        if i > l-1:
            return 0
        elif not str[i].isdigit():
            return 0
        while str[i].isdigit():
            i += 1
            if i > l-1:
                break
        p = int(str[j: i])
        if p < -2147483648:
            return -2147483648
        elif p > 2147483647:
            return 2147483647
        return p


s = Solution()
string = "    +1"
print(s.myAtoi(string))
print(string.strip())
