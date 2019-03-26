# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []:
            return None
        r = len(nums)//2
        left_tree = nums[:r]
        right_tree = nums[r+1:]
        root = TreeNode(nums[r])
        root.left = self.sortedArrayToBST(left_tree)
        root.right = self.sortedArrayToBST(right_tree)
        return root


s = Solution()
root = s.sortedArrayToBST([-10, -3, 0, 5, 9])
print(root.val)
print(root.left.val)
print(root.right.val)
print(root.left.left.val)
print(root.right.left.val)
