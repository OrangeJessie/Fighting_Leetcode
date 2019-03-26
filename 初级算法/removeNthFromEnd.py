# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        for i in range(n):
            fast = fast.next
        slow = head
        if not fast:
            head = head.next
            return head
        else:
            node = slow
            while fast:
                node = slow
                fast = fast.next
                slow = slow.next
            node.next = slow.next
        return head

    # 速度很快，但是逻辑没有上面那个简单
    def removeNthFromEnd2(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        List = []
        count = 0
        while head:
            List.append(head)
            head = head.next
            count = count+1

        if count == 1:
            return None
        if List[-n].next is not None:
            List[-n-1].next = None
            return List[0]
        else:
            List[-n].val = List[-n].next.val
            List[-n].next = List[-n].next.next
        return List[0]


h = ListNode(1)
s = Solution()
print(s.removeNthFromEnd(h, 1))
