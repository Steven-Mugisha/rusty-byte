# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build_helper(preorder, inorder, low, high, p_index):
            if low > high:
                return None
            
            current_value = preorder[p_index[0]]
            p_index[0] += 1

            root = TreeNode(current_value)

            mid_index = inorder.index(current_value)

            if low == high: return root

            root.left = build_helper(preorder, inorder, low, mid_index - 1, p_index)
            root.right = build_helper(preorder, inorder, mid_index + 1, high, p_index)

            return root
        
        p_index = [0]

        return build_helper(preorder, inorder, 0, len(preorder) - 1, p_index)

            

            
            