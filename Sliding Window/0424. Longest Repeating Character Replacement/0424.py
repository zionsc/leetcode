# AABABBA
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int) # hashmap in order to keep track of the number of times a character appears
        res = 0 # length of the longest substring that can have k replacements to be the same character

        l = 0
        maxfrequency = 0 # to keep track of the most frequently appearing character

        for r in range(len(s)):
            count[s[r]] += 1 # append whatever is found first
            maxfrequency = max(maxfrequency, count[s[r]]) # update maxfrequency to be the newly updated character or whatever it was previously 
            # ^^ works as only an increase in any character would result in the maxfrequency getting replaced
            while (r - l + 1) - maxfrequency > k: # if the number of changes we need to make exceed k, then that length does not work, slide the window. -> l += 1
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
    
        return res


