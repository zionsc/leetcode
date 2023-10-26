# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return ""
        
        res = []
        q = deque([root])

        while q:
            node = q.popleft()
            if not node:
                res.append("null")
                continue
            res.append(str(node.val))

            q.append(node.left)
            q.append(node.right)
        
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        if not data:
            return None
        
        values = data.split(",")
        root = TreeNode(int(values[0]))
        q = deque([root])

        i = 1
        while q and i < len(values):
            node = q.popleft()

            # left child
            if values[i] != "null":
                left = TreeNode(int(values[i]))
                node.left = left
                q.append(left)
            i += 1

            # check if still in bounds
            if i >= len(values):
                break
            
            # right child
            if values[i] != "null":
                right = TreeNode(int(values[i]))
                node.right = right
                q.append(right)
            i += 1

        return root


    

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans