class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = [ d / s for d, s in zip(dist, speed) ]
        time.sort()

        for i in range(len(time)):
            # since the weapon takes out one per minute, if the time it takes for the ith monster is less than 
            # the number of monsters at that point, then we don't have enough time to take them out.
            if time[i] <= i:
                return i
        
        return len(time)
