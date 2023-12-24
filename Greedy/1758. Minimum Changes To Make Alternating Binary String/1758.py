class Solution:
    def minOperations(self, s: str) -> int:
        # essentially the string has to start with and alternate or start with 1 and alternate.
        # essentially check do 0's belong in the evens or do 1's belong in the evens? which one is minimum
        even0, even1 = 0,0

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '0':
                    even1 += 1
                else: # elif s[i] == '1'
                    even0 += 1
            else:
                if s[i] == '0':
                    even0 += 1
                else:
                    even1 += 1
        return min(even0, even1)