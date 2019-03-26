# 电话号码的字母组合
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 示例:
#
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        digit2chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = [i for i in digit2chars[digits[0]]]
        for i in digits[1:]:
            res = [m+n for m in res for n in digit2chars[i]]
            print(res)
        return res

    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dtos_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ld = len(digits)
        all_str = []
        if ld == 1:
            for i in dtos_dict[digits[0]]:
                all_str.append(i)
            return all_str
        for i in dtos_dict[digits[0]]:
            for j in dtos_dict[digits[1]]:
                all_str.append(i+j)
        for i in range(2, ld):
            sub_str = []
            for j in all_str:
                for k in dtos_dict[digits[i]]:
                    sub_str.append(j+k)
            all_str = sub_str
        return all_str
