# 填充每个节点的下一个右侧节点指针
# 给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
# 初始状态下，所有 next 指针都被设置为 NULL。

# 提示：
#
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    # 比较传统的层次遍历，浪费大量时间再节点添加到列表中
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        stack = [root]
        while stack:
            ln = len(stack)
            layer_list = []
            for node in range(ln):
                if stack[node].left:
                    layer_list.append(stack[node].left)
                    layer_list.append(stack[node].right)
                if node < ln - 1:
                    stack[node].next = stack[node+1]
            stack = layer_list
        return root

    def connect2(self, root):
        # 看了下速度最快的代码，实现思路和我的层次遍历不一样
        # 那份代码本质上也是层次遍历，但实现思路上更加巧妙，且浪费的空间更少
        # 下面代码是那份参考代码
        if not root:
            return
        prev = root  # 用prev来记录每一行的头节点
        while prev.left:
            current = prev  # 用current对每一行进行遍历
            # 每一行的遍历是利用了next属性，避免了（传统层次遍历方法）从队列中弹出节点，节约了时间
            while current:
                current.left.next = current.right
                if current.next:
                    current.right.next = current.next.left
                current = current.next
            prev = prev.left
