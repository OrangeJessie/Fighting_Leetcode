# Task Scheduler
# 给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。
#
# 然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
#
# 你需要计算完成所有任务所需要的最短时间。
#
# 示例 1：
#
# 输入: tasks = ["A","A","A","B","B","B"], n = 2
# 输出: 8
# 执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # 只需要输出总时间，可以用出现次数最多的来分段，段数为最多次-1，中间间隔为n+出现次数最多的个数即
        # 出现次数最多的不一定是一个，可能是多个
        if not tasks:
            return 0
        dic = {}
        # 存列表就可以了
        for i in tasks:
            try:
                dic[i] += 1
            except:
                dic[i] = 1
        max_val = 0
        count = 1
        for i in dic.values():
            if i > max_val:
                max_val = i
                count = 1
            elif i == max_val:
                count += 1
        return max((max_val-1)*(1+n)+count, len(tasks))
