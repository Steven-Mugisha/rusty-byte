# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        q = [(root, 0)]
        ans = []

        while q:
            node, level = q.pop(0)
            if len(ans) <= level:
                ans.append([])
            ans[level].append(node.val)
            for child in [node.left, node.right]:
                if child:
                    q.append((child, level + 1))
        
        return ans