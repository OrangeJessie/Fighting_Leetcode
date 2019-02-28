# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def addlist(self, head, b):
        for i in b:
            p = ListNode(i)
            head.next = p
            head = head.next


class Solution:
    # 迭代的方式
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        temp = head.next
        if not temp:
            return head
        temp2 = temp.next
        head.next = None
        while temp:
            if temp2:
                temp.next = head
                head = temp
                temp = temp2
                temp2 = temp.next
            else:
                temp.next = head
                head = temp
                break
        return head

    # 递归的方式——从链表的最后两位开始向前反转
    def reverseList2(self, head):
        if (not head) or (not head.next):
            return head
        # elif not head.next:
        #     return head
        temp = self.reverseList2(head.next)          # temp是新链表的开头
        head.next.next = head                       # 这个地方temp不能移动
        head.next = None                            # 为了使递归在新链表完成后结束，需要使head.next始终指向None
        return temp


head = ListNode(1)
head.addlist(head, [2, 3, 4, 5])
s = Solution()
head = s.reverseList2(head)
while head:
    print(head.val)
    head = head.next

