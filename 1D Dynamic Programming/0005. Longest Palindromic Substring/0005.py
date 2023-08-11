class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        # basically go through all possible start points within the string, start at that startpoint, expend outwards
        # for each possible substring.
        # we do not have to check whether it is odd or even because the palindrome checks will do our job for us

        for i in range(len(s)):

            # odd length palindromes
            l, r = i, i # start at i and expand outwards
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l:r + 1]
                    # expand outwards with the start location still being at i
                    l -= 1
                    r += 1 

            # even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l:r + 1]
                    # expand outwards with the start location still being at i and i + 1 (since it is even)
                    l -= 1
                    r += 1

        return res