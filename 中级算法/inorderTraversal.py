# 给定一个二叉树，返回它的中序 遍历。
# 示例:
#
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,3,2]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    # 递归算法
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        tree = []
        if not root:
            return tree
        if root.left:
            tree += self.inorderTraversal(root.left)
        tree.append(root.val)
        if root.right:
            tree += self.inorderTraversal(root.right)
        return tree

    # 迭代算法
    def inorderTraversal2(self, root):
        if not root:
            return []
        res = []
        point = root
        stack = []
        while point:
            if point.left:
                stack.append(point)
                point = point.left
            else:
                res.append(point.val)
                if point.right:
                    point = point.right
                    continue
                else:
                    while stack and not point.right:
                        point = stack.pop()
                        res.append(point.val)
                    if not point.right:                 # 是因为stack里没有元素而停止循环
                        return res
                    else:                               # 当前节点有右节点
                        point = point.right
