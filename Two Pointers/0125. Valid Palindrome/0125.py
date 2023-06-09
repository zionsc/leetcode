class Solution:
    def isPalindrome(self, s: str) -> bool:

        # METHOD 1: Reverse String

        # newStr = ""
        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower()
        # return newStr == newStr[::-1]


        # METHOD 2: Two-Pointer Method

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]): # Must use self.somehing when calling another function inside of an object
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    # Could write own alpha-numeric function 
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )

            


        


