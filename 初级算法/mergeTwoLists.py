# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def addnode(self, head, x):
        for i in x:
            s = ListNode(i)
            head.next = s
            head = head.next


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1 = l1.next
        merge = head
        while l1 and l2:
            if l1.val > l2.val:
                head.next = l2
                head = head.next
                l2 = l2.next
            else:
                head.next = l1
                head = head.next
                l1 = l1.next
        while l1:
            head.next = l1
            head = head.next
            l1 = l1.next
        while l2:
            head.next = l2
            head = head.next
            l2 = l2.next
        return merge


h1 = ListNode(1)
h1.addnode(h1, [2, 4])
h2 = ListNode(1)
h2.addnode(h2, [3, 4])
s = Solution()
h3 = s.mergeTwoLists(h1, h2)
while h3:
    print(h3.val)
    h3 = h3.next
