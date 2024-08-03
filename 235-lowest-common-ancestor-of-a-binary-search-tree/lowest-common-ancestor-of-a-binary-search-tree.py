# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # while True:
        #     if root.val < p.val and root.val < q.val:
        #         root = root.right
            
        #     elif root.val > p.val and root.val > q.val:
        #         root = root.left
            
        #     else:
        #         return root

        if not root: return None

        if root.val == p.val or root.val == q.val:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left:
            return right
        
        if not right:
            return left
        
        return root
