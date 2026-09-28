# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(node, lower_bound, upper_bound):

            if not node:
                return True

            if not (lower_bound < node.val < upper_bound):
                return False

            
            left = isValid(node.left, lower_bound, node.val)
            right = isValid(node.right, node.val, upper_bound)

            return left and right
        
        return isValid(root, float("-inf"), float("inf"))

            
