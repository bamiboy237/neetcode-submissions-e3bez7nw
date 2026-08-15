# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0
        
        def dfs(node, depth):
            nonlocal maxDepth
            if not node:
                return
            
            depth += 1

            if node.left is None and node.right is None:
                maxDepth = max(depth, maxDepth)

            dfs(node.left, depth)
            dfs(node.right, depth)

        if not root:
            return 0
        dfs(root, 0)

        return maxDepth