class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        m = p = g = 0
        travelm = travelp = travelg = 0
        
        for i in range(len(garbage)):
            for j in range(len(garbage[i])):
                if garbage[i][j] == "M":
                    m += 1
                    travelm = i
                elif garbage[i][j] == "P":
                    p += 1
                    travelp = i
                elif garbage[i][j] == "G":
                    g += 1
                    travelg = i
        
        for i in range(1, len(travel)):
            travel[i] += travel[i - 1]
        
        travelm = travel[travelm - 1] if travelm != 0 else 0
        travelp = travel[travelp - 1] if travelp != 0 else 0
        travelg = travel[travelg - 1] if travelg != 0 else 0

        return m + travelm + p + travelp + g + travelg

        