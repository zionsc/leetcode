class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prev = [1]

        for i in range(1, rowIndex + 1):
            curr = [1] # every row starts with 1

            for j in range(1, len(prev)):
                curr.append(prev[j - 1] + prev[j])
            
            curr.append(1) # every row ends with 1
            prev = curr

        return prev

        