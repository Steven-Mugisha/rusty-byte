# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(pre, ino, low, high, mapIdx, pIdx):
            if low > high:
                return
            
            currVal = pre[pIdx[0]]
            pIdx[0] += 1

            root = TreeNode(currVal)

            if low == high: return root

            midIdx = mapIdx[currVal]

            root.left = dfs(pre, ino, low, midIdx - 1, mapIdx, pIdx)
            root.right = dfs(pre, ino, midIdx + 1, high, mapIdx, pIdx)

            return root
        
        mapIdx = dict()
        pIdx = [0]

        for val in range(len(preorder)):
            mapIdx[inorder[val]] = val
        
        return dfs(preorder, inorder, 0, len(preorder) - 1, mapIdx, pIdx)