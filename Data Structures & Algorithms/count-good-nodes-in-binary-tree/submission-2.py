# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = [0]

        def dfs(node, max_parent):
            if node is None:
                return 0

            if node.val >= max_parent:
                max_parent = node.val
                good_nodes[0] += 1

            dfs(node.left, max_parent)
            dfs(node.right, max_parent)

            return
        dfs(root, float('-inf'))
        return good_nodes[0]
            