# 二叉搜索树中第K小的元素
# 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
#
# 说明：
# 你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
#
# 示例 1:
#
# 输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 1


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    # 中序遍历二叉搜索树就是从小到大排列的
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return None
        stack = []
        count = 0
        cur = root
        while cur:
            if cur.left:
                stack.append(cur)
                cur = cur.left
            else:
                count += 1
                if count == k:
                    return cur.val
                if cur.right:
                    cur = cur.right
                    continue
                else:
                    while stack and not cur.right:
                        cur = stack.pop()
                        count += 1
                        if count == k:
                            return cur.val
                    if cur.right:
                        cur = cur.right

    # 递归相当于先中序遍历
    def kthSmallest2(self, root, k):
        res = []
        self.search(res, root)
        return res[k-1]

    def search(self, res, root):
        if not root:
            return
        self.search(res, root.left)
        res.append(root.val)
        self.search(res, root.right)
