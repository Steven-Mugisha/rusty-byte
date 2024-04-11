# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        root = self.__delete_node(root, key)
        return root
    
    def __find_min(self, current_node):
        while current_node.left:
            current_node = current_node.left
        
        return current_node.val

    def __delete_node(self, current_node, key):
        if current_node is None:
            return None

        if key < current_node.val:
            current_node.left = self.__delete_node(current_node.left, key)

        elif key > current_node.val:
            current_node.right = self.__delete_node(current_node.right, key)

        else:
            if current_node.left is None and current_node.right is None:
                return None

            elif current_node.left is None:
                current_node = current_node.right

            elif current_node.right is None:
                current_node = current_node.left

            else:
                sub_tree_min = self.__find_min(current_node.right)
                current_node.val = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)

        return current_node