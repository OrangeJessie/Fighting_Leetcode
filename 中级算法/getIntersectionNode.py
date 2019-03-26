# 相交链表
# 编写一个程序，找到两个单链表相交的起始节点。

# 示例：
# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
# 输出：Reference of the node with value = 8
# 输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。
# 从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
# 在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

# 注意：
# 如果两个链表没有交点，返回 null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    # 通过两个链表的长度差来判断交叉点之前的节点数
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        hA = headA
        hB = headB
        la = 1
        lb = 1
        while headA:
            la += 1
            headA = headA.next
        while headB:
            lb += 1
            headB = headB.next
        d = la - lb
        if d > 0:
            while d > 0:
                hA = hA.next
                d -= 1
        elif d < 0:
            while d < 0:
                hB = hB.next
                d += 1
        while hA:
            if hA == hB:
                return hA
            hA = hA.next
            hB = hB.next
        return None

