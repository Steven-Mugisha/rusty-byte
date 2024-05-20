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
        stream = []
        def ser_rec(root):
            if not root:
                stream.append("N")
                return 
            stream.append(str(root.val))
            ser_rec(root.left)
            ser_rec(root.right)

        ser_rec(root)
        return ",".join(stream)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        stream = data.split(",")
        self.index = 0

        def des_rec():
            if stream[self.index] == "N":
                self.index += 1
                return None
            
            root = TreeNode(int(stream[self.index]))
            self.index += 1
            root.left = des_rec()
            root.right = des_rec()

            return root

        root = des_rec()

        return root
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))