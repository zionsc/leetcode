class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack=[]
        currRoot=-1

        for node in preorder:
            while stack and node>stack[-1]:
                currRoot=stack.pop()

            if node<=currRoot:
                return False

            stack.append(node)
            
        return True