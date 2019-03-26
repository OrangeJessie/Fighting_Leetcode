# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for i in strs:
            li = []
            for j in i:
                li.append(j)
            len_i = len(li)
            for p in range(len_i):
                for k in range(p+1, len_i):
                    if li[p] > li[k]:
                        temp = li[p]
                        li[p] = li[k]
                        li[k] = temp
            ss = ''.join(li)
            if ss in d:
                d[ss].append(i)
            else:
                d[ss] = [i]
        return list(d.values())

    def groupAnagrams2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for x in strs:
            sorted_x = "".join(sorted(x))
            if sorted_x in dic:
                dic[sorted_x].append(x)
            else:
                dic[sorted_x] = [x]

        return list(dic.values())


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


