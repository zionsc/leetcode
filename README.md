ARRAY & HASHING
0217. Contains Duplicate: Hashset to determine if it appears more than once
0242. Valid Anagram: Hashmap to determine if str1 has same num of each char as str2
0001. Two Sum: Hashmap to find index
0049. Group Anagrams: count[0] * 26 to determine ID of each anagram (with ord(c) - ord('a')), then tuple as list cannot be used as a key in hashmap
0347. Top K Frequent Elements: Bucketsort into array (index is number of times it pops up), keep track of the number in a hashmap to use the array. for i in range(len(nums)) is by reference, * len(nums) is copy --> do range times, copy it len times. 
0238. Product of Array Except Self: Iterate through twice to avoid O(n^2) runtime. Use Prefix and Postfix in order to avoid multiplying digit at index --> clever greedy algorithm, prefix multiplies everything infront, postfix multiplies everything behind.
0036. Valid Sudoku: Check rows/cols/squares with defaultdict(set) in order to check each individual row/col/square --> square key for each square should be
r//3 and c//3 as // is integer div to return 0 1 2 x 0 1 2 for each of the 9 squares, but / is float point division.
0659. Encode and Decode Strings: Length of string+delimeter in order to make each encode unique --> number is str[i:j] with j being the first # after the number (length of string) res.append(str[j+1 : j+1+length]), then i = j + 1 + length --> to find next #.
0128. Longest Consecutive Sequence: Check if number is the start of a sequence (if n-1 is not in set) --> while (n+length) is in set, length += 1 


STACK:
0020. Valid Parantheses: Hashmap that maps closing parenthesis to opening parenthesis --> iterate thru string, if stumble upon closing parenthesis, if not empty and 
stack[-1] (last item in stack) is the matching parenthesis, stack.pop(). Else return false as the closing and open do not match. If stumble upon open, simply just 
stack.append(). Return true only if stack is empty at the end, else return false. 
0155. Min Stack: Implement regular stack for the actual values, and a min stack for the min values at each index value. Pop from both, val = (val, minstack[-1] if min_stack else val) --> then minstack.append(val) --> basically the val is the minstack's most recent val if it is not empty. add the the current minimum val to the minstack. of course also add the actual given value to the first stack. this is o(1) as it simply uses two stacks, no iteration. 
0150. Evaluate Reverse Polish Notation: Have a stack, simply do the operation on the two most recent stack values. Division is not integer division, just simply truncated to 0 (rounded down always).
0022. Generate Parantheses: Base case, When open == close == n. case 1: open < n, case 2: close < open --> stack.append("(") backtrack(open + 1, close) and stack.pop(), add to stack and add it to the res (res.append("".join(stack))) in order to add it to a empty list to add to res. stack.pop() backtracks after it recursively goes through to the result