# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # recursive -> add to an array, sort the array, return array[k-1]
        res = []
        
        def dfs(node):
            nonlocal res
            if not node:
                return 
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        res.sort()
        return res[k-1]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iterative -> go left until possible, when return back, pop from stack -> go right when you can't go left -> n+=1
        # when n == k: return node.val
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1  
            
            if k == 0:
                return curr.val
            curr = curr.right