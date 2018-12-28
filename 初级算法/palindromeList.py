# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def palindromeList(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        b = []
        while head:
            b.append(head.val)
            head = head.next
        l = len(b)//2
        for i in range(l):
            if b[i] != b[-i-1]:
                return False
        return True

