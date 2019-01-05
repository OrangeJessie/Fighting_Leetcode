# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        val = []
        if not root:
            return val
        node_list = [[root]]
        while node_list != []:
            lay = node_list.pop(0)
            lay_val = []
            lay_list = []
            for i in lay:
                lay_val.append(i.val)
                if i.left:
                    lay_list.append(i.left)
                if i.right:
                    lay_list.append(i.right)
            val.append(lay_val)
            if lay_list != []:
                node_list.append(lay_list)
        return val

