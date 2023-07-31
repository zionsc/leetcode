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
        # creating a list from the string again
        vals = data.split(",")

        # create a global variable that is a part of the class in order to make sure to keep track of the 
        # iteration that we are on -> we cannot make it non-global because then it would reset.
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            # else if it not nullptr
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        root = dfs()
        return root
