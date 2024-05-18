# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data = []

        def preOrderSer(node):
            if not node:
                data.append("N")
                return
            
            data.append(str(node.val))
            preOrderSer(node.left)
            preOrderSer(node.right)
        
        preOrderSer(root)

        return ",".join(data)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        val = data.split(",")
        self.index = 0

        def preOrderDer():
            if val[self.index] == "N":
                self.index += 1
                return None

            
            root = TreeNode(int(val[self.index]))
            self.index += 1
            root.left = preOrderDer()
            root.right = preOrderDer()
            return root
        
        return preOrderDer()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))