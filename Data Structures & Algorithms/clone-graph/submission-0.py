"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return None

        copies = {}

        def dfs(original):
            if original in copies:
                return copies[original]

            copies[original] = Node(original.val)
            for neighbor in original.neighbors:
                copies[original].neighbors.append(dfs(neighbor))
            
            return copies[original]

        return dfs(node)