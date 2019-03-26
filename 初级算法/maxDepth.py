# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 构造一棵树喵喵喵
class Tree(object):
    def __init__(self):
        self.root = TreeNode(-1)
        self.queue = []

    def addNode(self, x):
        node = TreeNode(x)
        if self.root.val == -1:
            self.root = node
            self.queue.append(self.root)
        elif self.queue[0].left == None:
            self.queue[0].left = node
            self.queue.append(node)
        elif self.queue[0].right == None:
            self.queue[0].right = node
            self.queue.append(node)
            self.queue.pop(0)


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left == None and root.right == None:
            return 1
        depth_left = 1
        depth_right = 1
        if root.left != None:
            depth_left += self.maxDepth(root.left)
        if root.right != None:
            depth_right += self.maxDepth(root.right)
        depth = max(depth_left, depth_right)
        return depth


