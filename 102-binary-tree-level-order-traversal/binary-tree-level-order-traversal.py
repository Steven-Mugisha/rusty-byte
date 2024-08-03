# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        q = []
        q.append((root, 0))
        res = []

        while q:
            curr, level = q.pop(0)
            if len(res) <= level:
                res.append([])
            res[level].append(curr.val)

            for child in [curr.left, curr.right]:
                if child:
                    q.append((child, level + 1))
        
        return res