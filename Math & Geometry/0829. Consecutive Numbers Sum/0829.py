class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        res = 0
        for i in range(1, int(sqrt(2 * n)) + 1):
            if i % 2 == 1 and n % i == 0:
                res += 1
            elif i % 2 == 0 and n % i == i // 2:
                res += 1
        return res
"""
Starting the Loop (for i in range(1, int(sqrt(2 * n)) + 1)):
We start a loop with i, which will go from 1 up to a certain number. This number is decided by int(sqrt(2 * n)) + 1.
sqrt(2 * n) is like asking, "What is the square root of two times our number n?" This gives us a limit to how far we need to check. It's a bit like saying, "I only need to search this far to find all the answers."
Why this limit works is a bit complex, but it's based on how sums of numbers behave. It ensures we check all possible groups of numbers that could add up to n.
Checking Conditions (if and elif statements):
We check two different scenarios here - one for when i (the number of consecutive numbers we're adding) is odd and one for when it's even.
Odd Number of Terms (if i % 2 == 1 and n % i == 0):
% 2 == 1 is a way of asking, "Is i an odd number?"
n % i == 0 checks if n can be divided evenly by i. This is important because when the number of terms is odd, the middle term needs to be a factor of n for them to add up to n.
For example, if n = 15 and i = 3, we have 3 consecutive numbers (4, 5, 6) where 5 (the middle number) is a factor of 15.
Even Number of Terms (elif i % 2 == 0 and n % i == i // 2):
% 2 == 0 is asking, "Is i an even number?"
n % i == i // 2 is a bit trickier. It's checking a special condition that must be true for even-length sequences of numbers to add up to n. It's ensuring that the way we split n into i parts leaves a remainder that fits a specific pattern.
Counting (res += 1):
Whenever we find a group of numbers that add up to n, we add 1 to our count (res).
Returning the Result (return res):
At the end, we return res, which now holds the number of different ways n can be written as the sum of consecutive numbers.
"""