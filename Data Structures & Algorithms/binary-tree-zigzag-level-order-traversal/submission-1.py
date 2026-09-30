# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        left_to_right = True
        traversal = []

        queue = deque([root])

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)   
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if left_to_right:
                traversal.append(level)
            else:
                traversal.append(level[::-1])

            left_to_right = not left_to_right

        return traversal
                