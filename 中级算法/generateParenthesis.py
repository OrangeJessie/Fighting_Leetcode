# 生成括号
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution(object):
    # 生成所有小于n的，时间复杂度很高
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        generate_list = ['()']
        for i in range(1, n):
            sub_list = []
            for combination in generate_list:
                for j in range(2*i):
                    if combination[j] == ')':
                        newstr = combination[:j]+'()'+combination[j:]
                        newstr2 = combination[:j+1]+'()'+combination[j+1:]
                        if newstr not in sub_list:
                            sub_list.append(newstr)
                        if newstr2 not in sub_list:
                            sub_list.append(newstr2)
            generate_list = sub_list
        return generate_list

    # 直接生成n，时间复杂度较低
    def generateParenthesis2(self, n):
        res_list = []
        self.DFS(n, n, '', res_list)
        return res_list

    def DFS(self, left, right, s, res):
        if left == 0 and right == 0:
            res.append(s)
        else:
            if left > 0:
                self.DFS(left-1, right, s+'(', res)
            if right > left:                            # 有左括号没有被匹配
                self.DFS(left, right-1, s+')', res)
