# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def addList(self, head, b):
        node = head
        for i in b:
            node.next = ListNode(i)
            node = node.next


class Solution:
    # 空间复杂度为O(n)，把链表的值存入数组，再用数组判断
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

    # 空间复杂度为O(1)，将链表后半段反向
    def palindromeList2(self, head):
        if not head:
            return True
        if not head.next:
            return True
        count = 0
        fast = head
        slow = head
        while head:
            count += 1
            head = head.next
        l1 = count//2
        l2 = count - l1
        for i in range(l2):
            fast = fast.next
        f2 = fast.next
        while f2:
            f3 = f2.next
            f2.next = fast
            fast = f2
            f2 = f3
        for i in range(l1):
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next
        return True

    def palindromeList3(self, head):
        if head == None or head.next == None:
            return True

        lat = head.next
        pre = head
        while lat != None and lat.next != None:
            lat = lat.next.next
            pre = pre.next

        cur = pre.next
        pre.next = None
        p = None
        while cur != None:
            q = cur.next
            cur.next = p
            p = cur
            cur = q

        while p != None and head != None:
            if p.val != head.val:
                return False
            p = p.next
            head = head.next

        return True


pl = ListNode(1)
pl.addList(pl, [1, 2, 1])
s = Solution()
print(s.palindromeList2(pl))
