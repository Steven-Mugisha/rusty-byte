# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        q = [root]
        ans = []

        while q:
            temp_q = q
            q = []
            level_nodes = []


            for node in temp_q:
                level_nodes.append(node.val)
            
            ans.append(level_nodes)

            for _ in range(len(temp_q)):
                curr_node = temp_q.pop(0)

                if curr_node.left:
                    q.append(curr_node.left)
                
                if curr_node.right:
                    q.append(curr_node.right)
        
        return ans 





