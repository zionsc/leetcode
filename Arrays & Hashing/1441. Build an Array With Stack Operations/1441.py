class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        currNum = 1
        index = 0

        while currNum <= n and index < len(target):
            num = target[index]
            if currNum == num:
                res.append("Push")
                currNum += 1
                index += 1
            else:
                res.append("Push")
                res.append("Pop")
                currNum += 1
        
        return res