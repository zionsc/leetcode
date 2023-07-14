class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        # step 1: make a count on what values are in each string

        s1Count, s2Count = [0] * 26, [0] * 26

        for s in s1:
            # for each the first window --> update the values to how many of each character appears
            s1Count[s1[s] - ord('a')] += 1
            s2Count[s2[s] - ord('a')] += 1

        matchCount = 0
        
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matchCount += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            # this cannot check the last iteration, so make sure to check before returning at the end of the funct
            if matchCount == 26:
                return True

            # update s2Count based on the new window --> update window after as we need access right now
            s2Count[s2[r] - ord('a')] += 1
            if s2Count[s[r] - ord('a')] == s1Count[s[r] - ord('a')]:
                matchCount += 1
            # this is because we increased it. It can only be greater or equal to. as s1[whatever] will be 1 or 0
            elif s2Count[s[r] - ord('a')] > s1Count[s[r] - ord('a')]:
                matchCount -= 1
            
            s2Count[s[l] - ord('a')] -= 1
            if s2Count[s[l] - ord('a')] == s1Count[s[l] - ord('a')]:
                matchCount += 1
            elif s2Count[s[l] - ord('a')] < s1Count[s[l] - ord('a')]:
                matchCount -= 1

            # now update the l pointer
            l += 1
            
        return matchCount == 26

