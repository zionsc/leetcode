class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        temp = [c for c in currentState]
        res = []
        for i in range(0, len(temp)):
            if i + 1 < len(temp) and temp[i] != '-' and temp[i + 1] != '-':
                temp[i], temp[i + 1] = '-', '-' 
                balls = "".join(temp)
                res.append(balls)
                temp[i],temp[i + 1] = '+', '+'
        return res