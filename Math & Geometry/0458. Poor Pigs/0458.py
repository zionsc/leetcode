class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # number of attempts we have
        attempts = minutesToTest // minutesToDie

        # initially check how many pigs are minimum, start at 0!
        pigs = 0
        
        # because each pig can check numattempts + 1 buckets --> 1 pig can check 2 buckets with 1 attempt, 1 pig can check 3 buckets with 2 attempts, 2 pigs can check 4 buckets with 1 attempt -> 2 pigs can check 9 buckets! thus, attempts + 1 ^ pigs < buckets checks for until we can check with the given number of pigs
        while (attempts + 1) ** pigs < buckets:
            pigs += 1
        return pigs
