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
        node_completed = {}

        def clone_helper(node):
            if not node:
                return None
            
            cloned_node = Node(node.val)
            node_completed[node] = cloned_node

            for nei in node.neighbors:
                curr_node = node_completed.get(nei)
                if not curr_node:
                    cloned_node.neighbors.append(clone_helper(nei))

                else:
                    cloned_node.neighbors.append(curr_node)
            
            return cloned_node
        
        return clone_helper(node)

