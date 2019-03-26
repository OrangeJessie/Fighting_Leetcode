# 二叉树的序列化与反序列化
# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
#
# 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
#
# 示例:
#
# 你可以将以下二叉树：
#
#     1
#    / \
#   2   3
#      / \
#     4   5
#
# 序列化为 "[1,2,3,null,null,4,5]"
# 提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
#
# 说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # 利用栈来前序遍历树
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        node_stack = [[root]]
        val_list = []
        while node_stack:
            node = node_stack.pop(0)
            node_list = []
            for i in node:
                if not i:
                    val_list.append(None)
                else:
                    val_list.append(i.val)
                    if i.left:
                        node_list.append(i.left)
                    else:
                        node_list.append(None)
                    if i.right:
                        node_list.append(i.right)
                    else:
                        node_list.append(None)
            for j in node_list:
                if j:
                    node_stack.append(node_list)
                    break
        return val_list

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        tree_root = TreeNode(data[0])
        ld = len(data)
        count = 1
        node_stack = [[tree_root]]
        while node_stack:
            node_list = node_stack.pop(0)
            append_list = []
            for node in node_list:
                if count < ld:
                    if data[count] != None:
                        node.left = TreeNode(data[count])
                        append_list.append(node.left)
                    if data[count+1] != None:
                        node.right = TreeNode(data[count+1])
                        append_list.append(node.right)
                    count += 2
            if append_list:
                node_stack.append(append_list)
        return tree_root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
