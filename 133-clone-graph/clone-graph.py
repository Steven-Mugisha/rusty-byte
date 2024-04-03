"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        nodes_completed = {}

        def cloneGraph_helper(node):
            if node is None:
                return None

            cloned_node = Node(node.val)
            nodes_completed[node] = cloned_node

            for p in node.neighbors:
                x = nodes_completed.get(p)
                if not x:
                    cloned_node.neighbors += [cloneGraph_helper(p)]
                
                else:
                    cloned_node.neighbors += [x]

            return cloned_node

        return cloneGraph_helper(node)






       