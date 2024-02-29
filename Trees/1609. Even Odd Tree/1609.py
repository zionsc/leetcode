# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]

        level = 0
        while queue:
            new_queue = []
            curr_level = [node.val for node in queue]
            print(curr_level, level)
            if level % 2 == 0:
                if curr_level[0] % 2 == 0:
                    return False
                for i in range(1, len(curr_level)):
                    if curr_level[i] <= curr_level[i - 1] or curr_level[i] % 2 == 0 or curr_level[i - 1] % 2 == 0:
                        return False
            elif level % 2 != 0:
                if curr_level[0] % 2 != 0:
                    return False
                for i in range(1, len(curr_level)):
                    if curr_level[i] >= curr_level[i - 1] or curr_level[i] % 2 != 0 or curr_level[i - 1] % 2 != 0:
                        return False
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue.copy()
            level += 1
        
        return True
                

            
                
