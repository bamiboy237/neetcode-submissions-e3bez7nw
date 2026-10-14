# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node, lower, upper):
            if node is None:
                return True

            if not lower < node.val < upper:
                return False

            return (inorder(node.left, lower, node.val) and inorder(node.right, node.val, upper))
        return inorder(root, float('-inf'), float('inf'))