# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        r_side = []

        self.dfs(root, r_side, 0)
        return r_side


    def dfs(self, root, r_side, level):

        if not root: return None

        if level == len(r_side):
            r_side.append(root.val)
        
        self.dfs(root.right, r_side, level + 1)
        self.dfs(root.left, r_side, level + 1)
        
        

        # for child in [root.right, root.left]:
        #     if child:
        #         self.dfs(child, r_side, level + 1)
        
