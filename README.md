ARRAY & HASHING: theres a trick to each question, maybe sorting, maybe using some trick for array
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


STACK: maybe use more than 1 stack? maybe use recursion
0020. Valid Parantheses: Hashmap that maps closing parenthesis to opening parenthesis --> iterate thru string, if stumble upon closing parenthesis, if not empty and 
stack[-1] (last item in stack) is the matching parenthesis, stack.pop(). Else return false as the closing and open do not match. If stumble upon open, simply just 
stack.append(). Return true only if stack is empty at the end, else return false. 
0155. Min Stack: Implement regular stack for the actual values, and a min stack for the min values at each index value. Pop from both, val = (val, minstack[-1] if min_stack else val) --> then minstack.append(val) --> basically the val is the minstack's most recent val if it is not empty. add the the current minimum val to the minstack. of course also add the actual given value to the first stack. this is o(1) as it simply uses two stacks, no iteration. 
0150. Evaluate Reverse Polish Notation: Have a stack, simply do the operation on the two most recent stack values. Division is not integer division, just simply truncated to 0 (rounded down always).
0022. Generate Parantheses: Base case, When open == close == n. case 1: open < n, case 2: close < open --> stack.append("(") backtrack(open + 1, close) and stack.pop(), add to stack and add it to the res (res.append("".join(stack))) in order to add it to a empty list to add to res. stack.pop() backtracks after it recursively goes through to the result
0739. Daily Temperatures: for i, t in enumerate(temperatures) gets the index and the value! Use a res list and a stack. Keep track of values until bigger values comes along in stack, update each index value pair that was skipped over (skipped over means not in res list but added to the stack) basically use a stack and a result list
0853. Car Fleet: Can pair two lists together by doing pair = [[p, s] for i in zip(position, speed)]. WOW! Can also iterate through the sorted list (in reverse order) by doing for p, s in sorted(pair)[::-1] or sorted(pair, reverse = True) --> stack.append((target - p) / s) to append the time and then compare the times whenever there is 2 or more in the stack. Cars behind will never go ahead of the front car of the fleet, so pop the ones that are part of the same fleet, but not at the top. if len(stack) >= 2 and stack[-1] <= stack[-2] then stack.pop() --> this is because stack[-1] will be behind stack[-2] in terms of a linear line. so we must hceck if stack[-1] (most recent car that we are checking) will be reaching target faster (will catch up and be a part of the same fleet) --> return len(stack), also since it is stack[-1] vs stack[-2] : it will be checking stack[-2] (which is most recent car fleet) vs stack[-1] (most recent car we are checking)
0084. Largest Rectangle in Histogram: Keep track of a maxArea. Have the stack be a pair (start index of rectangle, height of rectangle) for each bar. For each i, h in the histogram, start = i initialize the start to the index that the bar was discovered at (unless changed later). If the stack is not empty and the height of the newly discovered bar is < the stack[-1][1] (height of the most recent stack rectangle), then index, height = stack.pop() --> pop from the stack and keep track of the values in order to update maxArea. Update maxArea = max(maxArea, h * (i - index)) --> this is because i is the current bar that we found (we stopped the rectangle's growth here) and index is the value that the rectangle started at (this was initialized to start, but then start was updated as necessary!). Then start = index --> in order to update the start value to extend backwards as the current bar can extend backwards to the bar that was popped from the stack (as the popped bar was higher in height (taller) ). Keep repeating through this while loop until the bar that we discovered cannot be extended further back anymore. Then simply stack.append((start, i)) in order to add this to the stack. For all the values that still remain in the stack after iterating through the histogram, check the maxArea = max(maxArea, h * (len(heights) - i)) in order to check their area against the maxArea as they extend to the end of the histogram as they did not have any other bar that was less than them, meaning that they could extend to the len(heights).


TWO-POINTERS: maybe sort and keep track of some min/max in order to calculate the value (FIND THE TRICK!)
0125. Valid Palindrome: Left and Right Pointers, increment until you reach an alphanum --> create this by comparing ASCII values --> ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9') --> only for recursion you can have another function inside another function, when calling non-recursively, make sure to make it a separate helper function and call it with self.alphaNum(c) --> must do that when calling other functions from an object in python.
0167. Two Sum II: Basically use the idea that it is sorted. Pointers left and right, increment and decrement based on whether the numbers[l] + numbers[r] > or < to target (CAN do this because it is sorted). If it 
is > target, then r -= 1. If it is < target, then l += 1 (AS IT IS SORTED in INCREASING ORDER) --> else return [l + 1, r + 1] --> as they want 1 indexing.  
0015. 3Sum: Basically use the idea that we can sort the array in order to do the same operation as Two Sum II with a left and right pointer. Make sure a == nums[i - 1]: continue --> since we cannot have the same a twice with the same subset of numbers. at the end, make sure to do res.append([a, nums[l], nums[r]]) then l += 1 and r -= 1 then do a while loop for while nums[l] == nums[l - 1] and l < r: l += 1 (can also do for r instead) --> the reason for this is that we need to find the other subsets of a that are also valid answers that are not duplicates. 
0011. Container With Most Water: Basically have a left and right pointer, increment/decremet according to whatever is the shorter bar, maxArea = max(maxArea, min(height[l], height[r]) * (r - l)) -> because the min height bar will determine the max area. 
0042. Trapping Rain Water: Basically we want to keep track of a maxLeft and a maxRight. The reason for that is because we know that the smaller one will be the bottleneck. The furthest to the left and furthest to the right bars will hold min(furthestleft, furthestright) * whatever space there is available of water. Thus we know that we can increment the pointers accordingly. if maxLeft < maxRight: then l += 1 (increment the left pointer) maxLeft = max(maxLeft, height[l]) --> this will make sure we update the next left bottleneck. Then we can simply do result += (maxLeft - height[l]) -> this will make sure that we hold water if our current bar is lower than the bottleneck. Else if it is the same as the bottleneck, then we will simply not hold any water at all (res += 0)


BINARY SEARCH: Maybe perform binary search more than once
0704. Binary Search: Always use self.function() when calling a function inside of a class --> also everything in the binarysearch function should be inside if right >= left statement because it cannot go out of bounds. 
0074. Search a 2D Matrix: Find the row that it is contained in first. Then find the number within the row that it can be in. Return false is the row is not found at all.
0875. Koko Eating Bananas: Basic Idea is that any k value greater than max(piles) should be ignored as it does not help in improving the time. Do binary search for a value from l = 1, r = max(piles) as h could be super large, allowing k = 1 to also work. Simple binary search while l <= r. Need a for loop for p in pairs -> to see if k actual works in terms of being smaller or equal to hours. Do this by hours += math.ceil(p / k) --> math.ceil rounds up. Then check if hours <= h: res = min(res, k), r = k - 1 or else: l = k + 1
