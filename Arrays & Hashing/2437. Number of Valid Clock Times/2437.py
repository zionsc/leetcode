class Solution:
    def countTime(self, time: str) -> int:
        res = 1
        for i,t in enumerate(time):
            if t == '?':
                if i == 0:
                    if time[1] == '?':
                        res *= 24
                    elif time[1] < '4':
                        res *= 3
                    else:
                        res *= 2
                if i == 1:
                    if time[0] == '?':
                        continue
                    elif time[0] == '2':
                        res *= 4
                    else:
                        res *= 10
                if i == 3:
                    res *= 6
                if i == 4:
                    res *= 10
        return res
                    
    