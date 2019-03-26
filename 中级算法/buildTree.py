# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        divide = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:divide+1], inorder[:divide])
        root.right = self.buildTree(preorder[divide+1:], inorder[divide+1:])
        return root

    def buildTree2(self, preorder, inorder):
        if not preorder:
            return None
        stack = []          # 利用栈后进先出的原理
        root = TreeNode(preorder[0])
        stack.append(root)
        index = 0
        for i in range(1, len(preorder)):
            cur = stack[-1]
            if stack[-1].val != inorder[index]:          # 中序的第一个是最左的子树，表明该中序索引在左子树
                cur.left = TreeNode(preorder[i])
                stack.append(cur.left)
            else:
                while len(stack) != 0 and stack[-1].val == inorder[index]:      # 此时stack[-1] = 4，是cur的前一个
                    cur = stack.pop()                    # 以该点为根的子树没有右子树，表明该子树一表达完毕
                    index += 1
                if index < len(inorder):                 # 最后一步index可能大于inorder长度，大于时stack一定已经为0
                    cur.right = TreeNode(preorder[i])    # 此时cur = 2的节点
                    stack.append(cur.right)
        return root
