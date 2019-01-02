# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 两个指针，一个指针每次移动一步，另一个每次移动两步，在有环的情况下必然能相遇
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        fast = head
        slow = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    # 这个方法不太好，因为改变了原始的链表的类型
    def hasCycle2(self, head):
        if not head:
            return False
        while head:
            value = head.val
            if type(value) == str:
                return True
            head.val = str(value)
            head = head.next
        return False
