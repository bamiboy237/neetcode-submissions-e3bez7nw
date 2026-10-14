# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def find_path(node, target, path):
            if node is None:
                return False

            path.append(node)
            if node is target:
                return True

            if find_path(node.left, target, path):
                return True
            if find_path(node.right, target, path):
                return True

            path.pop()
            return False

        p_path = []
        q_path = []

        find_path(root, p, p_path)
        find_path(root, q, q_path)

        lca = None

        for p_node, q_node in zip(p_path, q_path):
            if p_node is not q_node:
                break
            lca = p_node

        return lca

            