# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    # 递归的方法
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left = root.left
        right = root.right
        return self.subRead(left, right)

    def subRead(self, left, right):
        if left == None and right == None:
            return True
        elif left == None and right != None:
            return False
        elif left != None and right == None:
            return False
        elif left.val != right.val:
            return False
        a = self.subRead(left.left, right.right)
        b = self.subRead(left.right, right.left)
        return a and b

    # 迭代的方法 速度比递归要快一点
    # 迭代的方式遍历整棵树
    def isSymmetric2(self, root):
        if not root:
            return True
        nodeList = [root.left, root.right]
        while nodeList:
            symmetricLeft = nodeList.pop(0)
            symmetricRight = nodeList.pop(0)
            if not symmetricLeft and not symmetricRight:
                continue
            if not symmetricLeft or not symmetricRight:
                return False
            if symmetricLeft.val != symmetricRight.val:
                return False
            nodeList.append(symmetricLeft.left)
            nodeList.append(symmetricRight.right)
            nodeList.append(symmetricLeft.right)
            nodeList.append(symmetricRight.left)
        return True
