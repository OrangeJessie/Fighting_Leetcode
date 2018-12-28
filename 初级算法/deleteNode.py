# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 常规情况下要先找到node的前一个node
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        tem_node = node.next
        node.val = tem_node.val
        node.next = tem_node.next

