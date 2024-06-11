# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildTreeHelper(preorder, inorder, left, right, mapping, p_index):
            if left > right:
                return 

            curr = preorder[p_index[0]]
            p_index[0] += 1
            in_index = mapping[curr]

            root = TreeNode(curr)
            if left == right: return root

            root.left = buildTreeHelper(preorder, inorder, left, in_index - 1, mapping, p_index)
            root.right = buildTreeHelper(preorder, inorder, in_index + 1, right, mapping, p_index)

            return root
        
        mapping, p_index = {} , [0]
        for i in range(len(preorder)):
            mapping[inorder[i]] = i
        
        return buildTreeHelper(preorder, inorder, 0, len(preorder) - 1, mapping, p_index)


