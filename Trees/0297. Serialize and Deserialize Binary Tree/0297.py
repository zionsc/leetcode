# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        # recursively go through with a delimeter being whatever, but in this case: ","
        res = []
        def dfs(root):
            if not root:
                res.append("N")
                return 
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        # appending it all to a string with each item being separated by ","
        return ",".join(res)

    def deserialize(self, data):
