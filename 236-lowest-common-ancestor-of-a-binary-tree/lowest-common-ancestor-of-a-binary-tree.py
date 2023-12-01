# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root:
            return root

        if p.val == root.val or q.val == root.val:
            return root

        left_solution = self.lowestCommonAncestor(root.left, p, q)
        right_solution = self.lowestCommonAncestor(root.right, p, q)

        if not left_solution:
            return right_solution
        
        if not right_solution:
            return left_solution

        return root 


        

        