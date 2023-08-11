class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        # basically go through all possible start points within the string, start at that startpoint, expend outwards
        # for each possible substring.
        # we do not have to check whether it is odd or even because the palindrome checks will do our job for us

        for i in range(len(s)):

            # odd length palindromes