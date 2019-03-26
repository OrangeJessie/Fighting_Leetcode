# 二叉树的锯齿形层次遍历
# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回锯齿形层次遍历如下：
#
# [
#   [3],
#   [20,9],
#   [15,7]
# ]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 存每一层节点的时候都按照从左到右的顺序，每一层节点val列表按照奇偶反序
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [[root]]
        val = []
        count = 0
        while stack != []:
            point = stack.pop(0)
            node = []
            sub_val = []
            sym = count % 2
            # if sym == 1:
            #     point = point[::-1]
            for i in point:
                sub_val.append(i.val)
                if i.left:
                    node.append(i.left)
                if i.right:
                    node.append(i.right)
            if node != []:
                stack.append(node)
            if sym == 0:
                val.append(sub_val)
            else:
                val.append(sub_val[::-1])
            count += 1
        return val
