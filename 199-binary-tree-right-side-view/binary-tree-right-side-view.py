# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def SideViewHelper(root, rightSideArr, level):
            if level == len(rightSideArr):
                rightSideArr.append(root.val)
            
            for child in [root.right, root.left]:
                if child:
                    SideViewHelper(child, rightSideArr, level + 1)
        
        if not root: return []
        
        rightSideArr = []
        SideViewHelper(root, rightSideArr, 0)
        
        return rightSideArr




