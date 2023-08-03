class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        currPartition = []

        def dfs(i):
            if i >= len(s):
                # if we got to the end, that means we can just add whatever it added as a palindrome
                res.append(currPartition.copy()) 
                return
            
            for j in range(i, len(s)): # check all from 0 to the end in order to see palindrome
                if self.isPalindrome(s, i, j):
                    currPartition.append(s[i:j+1]) # j + 1 because inclusive:exclusive, so to include j.
                    dfs(j + 1) # call this to check all the values between j and the end as well! -> palindromes could be inside
                    currPartition.pop() # clean up this recursive tree for the next iteration

        dfs(0)
        return res
    
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True