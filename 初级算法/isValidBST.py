# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
    # 对于每一层，把根节点的值规定为左子树最大值，右子树最小值
    def validBST(self, root, small, large):
        if root == None:
            return True
        if small >= root.val or large <= root.val:
            return False
        return self.validBST(root.left, small, root.val) and self.validBST(root.right, root.val, large)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.validBST(root, -2**32, 2**32-1)


t = Tree()
l = [10, 5, 15, 'null', 'null', 6, 20]
for i in l:
    t.addNode(i)
s = Solution()
print(s.isValidBST(t.root))
