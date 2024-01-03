class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        consecutive_lazers = []
        for i in range(len(bank)):
            count = bank[i].count('1')
            if count != 0:
                consecutive_lazers.append(count)
        
        for i in range(len(consecutive_lazers) - 1):
            res += consecutive_lazers[i] * consecutive_lazers[i + 1]
        return res
            
            