class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set() # to check if cycle

        def findHappy(numStr):
            if int(numStr) == 1:
                return True
            if int(numStr) in visited:
                return False
            
            res = 0
            visited.add(int(numStr))
            for n in range(len(numStr)):
                res += int(numStr[n]) ** 2
            
            return findHappy(str(res))
        
    
        return findHappy(str(n))