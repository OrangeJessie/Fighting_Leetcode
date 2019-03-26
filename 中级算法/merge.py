# 合并区间
# 给出一个区间的集合，请合并所有重叠的区间。
#
# 示例 1:
#
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    # 注意python中interval的用法
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        sorted_interval = self.sortInterval(intervals)
        merged = [sorted_interval[0]]

        for interval in sorted_interval[1:]:
            if interval.start <= merged[-1].end <= interval.end:
                merged[-1].end = interval.end
            elif merged[-1].end >= interval.end:
                continue
            else:
                merged.append(interval)
        return merged

    def sortInterval(self, intervals):
        ln = len(intervals)
        if ln <= 1:
            return intervals
        mid = ln//2
        interval1 = self.sortInterval(intervals[:mid])
        interval2 = self.sortInterval(intervals[mid:])
        sort_interval = self.mergeInterval(interval1, interval2)
        return sort_interval

    def mergeInterval(self, interval1, interval2):
        l1 = len(interval1)
        l2 = len(interval2)
        i = 0
        j = 0
        sort_interval = []
        while i < l1 and j < l2:
            if interval1[i].start < interval2[j].start:
                sort_interval.append(interval1[i])
                i += 1
            else:
                sort_interval.append(interval2[j])
                j += 1
        while i < l1:
            sort_interval.append(interval1[i])
            i += 1
        while j < l2:
            sort_interval.append(interval2[j])
            j += 1
        return sort_interval
