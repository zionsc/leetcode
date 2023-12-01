You are given four integers minLength, maxLength, oneGroup and zeroGroup.

A binary string is good if it satisfies the following conditions:

The length of the string is in the range [minLength, maxLength].
The size of each block of consecutive 1's is a multiple of oneGroup.
For example in a binary string 00110111100 sizes of each block of consecutive ones are [2,4].
The size of each block of consecutive 0's is a multiple of zeroGroup.
For example, in a binary string 00110111100 sizes of each block of consecutive ones are [2,1,2].
Return the number of good binary strings. Since the answer may be too large, return it modulo 109 + 7.

Note that 0 is considered a multiple of all the numbers.