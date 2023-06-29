0217. Contains Duplicate: Hashset to determine if it appears more than once
0242. Valid Anagram: Hashmap to determine if str1 has same num of each char as str2
0001. Two Sum: Hashmap to find index
0049. Group Anagrams: count[0] * 26 to determine ID of each anagram (with ord(c) - ord('a')), then tuple as list cannot be used as a key in hashmap
0347. Top K Frequent Elements: Bucketsort into array (index is number of times it pops up), keep track of the number in a hashmap to use the array. for i in range(len(nums)) is by reference, * len(nums) is copy --> do range times, copy it len times. 
0238. Product of Array Except Self: Iterate through twice to avoid O(n^2) runtime. Use Prefix and Postfix in order to avoid multiplying digit at index --> clever greedy algorithm
