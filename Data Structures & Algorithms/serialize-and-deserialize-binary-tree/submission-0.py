# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        data = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node is None:
                data.append("#")
            else:
                data.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)

        return ",".join(data)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])

        i = 1

        while queue:
            parent = queue.popleft()
            if values[i] != "#":
                parent.left = TreeNode(int(values[i]))
                queue.append(parent.left)

            i += 1

            if values[i] != "#":
                parent.right = TreeNode(int(values[i]))
                queue.append(parent.right)
            i += 1

        return root
