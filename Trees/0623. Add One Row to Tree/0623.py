# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        q=deque([(root,1)])

        if depth==1:
            newRoot=TreeNode(val)
            newRoot.left=root
            return newRoot

        while q:
            curr,level = q.popleft()
            if level==depth-1:
                q.appendleft((curr,level))
                break
            if curr.left:
                q.append((curr.left,level+1))
            if curr.right:
                q.append((curr.right,level+1))
        
        for curr,level in q:
            if curr.left:
                temp=curr.left
                curr.left=TreeNode(val)
                curr.left.left=temp
            else:
                curr.left=TreeNode(val)
            if curr.right:
                temp=curr.right
                curr.right=TreeNode(val)
                curr.right.right=temp
            else:
                curr.right=TreeNode(val)

        return root
                
