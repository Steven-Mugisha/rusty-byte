# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if root is None:
            return None
        
        # search the key from the tree:
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        elif root.val == key:
            if not root.left and not root.right:
                return None

            elif root.left is None:
                return root.right
            
            elif root.right is None:
                return root.left
                
            # choosing the right child
            small_node = self.traverse_helper(root.right)
            root.val = small_node.val
            root.right = self.deleteNode(root.right, small_node.val)

        
        return root
    
    def traverse_helper(self, node):
        while node.left:
            node = node.left
        return node
    
  
        
