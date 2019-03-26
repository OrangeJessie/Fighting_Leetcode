# 两数相加
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 原位为 r%10 进位为 r//10，方法2更好一点
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        r = l1.val+l2.val
        s = ListNode(r % 10)
        sym = r//10
        sc = s
        l1 = l1.next
        l2 = l2.next
        while True:
            if l1 and l2:
                if sym == 1:
                    r = l1.val+l2.val + 1
                else:
                    r = l1.val+l2.val
                s.next = ListNode(r % 10)
                sym = r//10
                l1 = l1.next
                l2 = l2.next
            elif l1:
                if sym == 1:
                    r = l1.val + 1
                else:
                    r = l1.val
                s.next = ListNode(r % 10)
                sym = r//10
                l1 = l1.next
            elif l2:
                if sym == 1:
                    r = l2.val + 1
                else:
                    r = l2.val
                s.next = ListNode(r % 10)
                sym = r//10
                l2 = l2.next
            else:
                if sym == 1:
                    s.next = ListNode(1)
                break
            s = s.next
        return sc

    # 依次判断l1和l2是否为None，加上不为None的值，carry为进位
    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
        return dummy.next
