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
0153. Find Minimum in Rotated Sorted Array: O(log n) time complex -> use binary search: trick is to use nums[mid] > nums[r] --> start of sequence is at the right subarray as it would have been rotated. nums[mid] < nums[r] --> start of sequence is at the left subarray
0033. Search in Rotated Sorted Array: Determine which side is sorted -> if mid >= left -> left is sorted else: -> right is sorted. within each case, check whether target is in not sorted side or else sorted side. left is sorted -> if target > mid or target < left. right is sorted -> target < mid or target > right
0981. Time Based Key-Value Store: Each key must hold a [value, timestamp] pair in a defaultdict(list) -> so that non-initialized keys have default empty lists. Set can just simply add the values by doing self.storage[key].append([value, timestamp]). Get basically initializes a res = "" in order to simply return res if it is not found as an empty string. values = self.storage.get(key, []) -> this basically gets the list of [value, timestamp] pairs within that specific key (of course, res would not be updated if the key did not exist, thus it is okay.) -> Do binary search within the timestamps of the list, and make sure to keep updating res as a valid timestamp comes up (less than or equal to but also close as it can be to the given input timestamp.) -> if values[mid][1] <= timestamp: res = values[mid][0], l = mid + 1 -> in order to check the right side because it is still valid up to then. Else: r = mid - 1 in order to search the left-side now since the values[mid]'s timestamp is larger. Simply return res. This will be empty if it did not find anything, but it will be something (closest but smallest (even can be at the timestamp itself if found)) if found. 
0004. Median of Two Sorted Arrays: Given two arrays, we need to find a partition of the total of both arrays in which we can calculate the median. We can do this by doing binary search on the smaller array in order to check if we have the correct partition of values from the left-side (Because partition of array A + parition of array B should be half of the array (left partition of the combined total array)). Check if the Amid > Bmid+1 -> then A has too many values -> do binary search with r = Amid - 1. If Bmid > Amid + 1 -> then B has too many values -> do binary search with l = mid + 1 --> the reason we do this is because to find the median, the left-side total partition will be in non-decreasing order (increasing) as the entire combined array must be sorted. If Amid <= Bmid + 1 and Bmid <= Amid + 1, then we have found the correct partition as the max values of the left partition of the total combined array are less than the min values of the right parition of the total combined right array -> if we have found the partition that is correct, we must check whether the length of the total combined array is odd or even --> if odd, then the median will be the middle value min(Amid + 1, Bmid + 1). if even, then it will be the two middle values divided by 2 (float division as we want a decimal) -> (max(Amid, Bmid) + min(Amid + 1, Bmid + 1) / 2) and we simply return one of those two values depending on what we found to be the cardinality of the modulo of the length of the combined array!


SLIDING WINDOW: WHILE loop to check something with l and r pointers!
0121. Best Time to Buy and Sell Stock: Basic idea is to have a l and r pointer, if l < r then there is a profit, thus update maxProfit accordingly, but else: update l = r as r is the smallest value found so far. Then for both cases update r += 1. 
0003. Longest Substring Without Repeating Characters: Use a two pointer system and check each substring, remove from the set until a the value is gone. for r in range(len(s)): while s[r] in set: l += 1, set.remove(s[l]) -> will start a new subset from the next val, can keep the ones that are not duplicates. set.add(s[r]), res = max(res, r - l + 1)
0424. Longest Repeating Character Replacement: Use a sliding window, set l = 0 and for r in range(len(s)) -> update hashmap (that keeps track of the number of values) -> map[s[r]] -> update the maxfrequency character as well: maxfreq = max(maxfreq, map[s[r]]) Since the only one that increased is the value at that point in the hashmap (key in hashmap). while (r - l + 1) - maxfreq > k: do map[s[l]] -= 1, l += 1 --> basically sliding the window to be smaller as that substring does not work. r - l + 1 is the length of the substring and it minus the maxfreq is the number of characters that need to be flipped in order to be repeating. This is because it would not be optimal to flip the most commonly occurring character. You do not need to decrement the maxfreq or to update the maxfreq at all at the sliding window step (l += 1) because maxfreq increasing is the only situation in which the resulting max length substring increases. This is because length of substring - maxfreq needs to be <= k, thus meaning maxfreq needs to increase to be as big as it possibly can be close to the size of the length. However, it being smaller would not help create a larger substring. -> res = max(res, r - l + 1) and this works at the end because the while loop makes sure that only valid substrings end up there for each r pointer. maxfreq is only updated when the length of the stirng actually increases, which is when there is a new r that we check. When the length is decreased, it only makes our potential res smaller. 
0567. Permutation in String: Keep a count of how many of each character comes out in s1 and s2 by doing s1Count, s2Count = [0] * 26, [0] * 26 -> then make sure to check how many matching characters there are (should be 26 since characters that don't appear in each one will end up being 0 and ones that do come out will be 1) Use a sliding window the size of s1 since s1 is our smaller string, and iterate through with the sliding window in s2 by doing r += 1 and l += 1. Make sure to update the matchCount when we update the sliding window. However, we do not have to re-iterate through the values, we can just make sure to see if the updated values ever changed, and change the matchCount accordingly. 
0076. Minimum Window Substring: Keep track of a need and a have integer in order to check if need == have. In order to check this, firstly add all values of t into a hashmap countT then need = len(countT) as we need the unique values of T (as duplicates do not count as long as we have atleast one of a character). Keep resLen = float("infinity") and res = [-1, -1] in order to make sure that we get the min value of resLen initially, and res because we need to make sure that l and r are updated into it. so whenever r - l + 1 < resLen: then res = [l, r] and resLen = r - l + 1. Make sure to only update have integer when countS[s[l]] < countT[s[l]] because we do not want to decrement it if we still have atleast one of that character in the window that we are focusing on at the time. However, while need == have, then make sure to shift the sliding window with l += 1 because we want to check what the minimum res of the window is that is still valid. 
0239. Sliding Window Maximum: In this question, we can use a queue (q = collections.deque()) in order to keep the line-up for the maximum values. l = r = 0, while r < len(nums): basically step 1: update the queue for the new right value: while nums[r] > nums[q[-1]]: q.pop() and then after that while has finished, then q.append(r) -> the reason we append the index and not the value itself is because we can access the value anytime by doing nums[r] but the index is not accessible, but we need it in order to check the left pointer (basically makes this very nice for us.) step 2: update the queue for the left pointer! basically if l > q[0]: (because since q[i] holds indexes, if l is greater than q[0] that means that the previous nums[l] was the max value (thus kept at the front of the queue) and that now we have shifted the window to the right by one, thus we no longer consider that old maximum) q.popleft(). step 3: update the output! basically if (r + 1) >= k: we do output.append(nums[q[-1]]) because l and r both start at 0, we need to make sure it gets to the size of the sliding window before updating it for each window, right? -> so basically it goes through step 1 and 2 until it gets to the correct size, then it goes to step 3 for every window. 


LINKED LIST: Iterative, can reverse list, use pointers as iterators, but also make dummy node and return dummy.next || OR find a cycle. 
0206. Reverse Linked List: Can solve iterative and recursively. Iterative is very easy, just have a prev, and curr pointer use temp and curr and prev and curr.next pointer and use basic logic to bump them around while curr: . -> recursive basically: keep track of the last value in the linkedList as newHead = self.reverseList(head.next) and then change the pointer to reverese by doing head.next.next = head all under if head.next:. then after that if, just make sure head.next points to nothing in order to remove the old pointer arrow, then return newHead (since we made sure to not change that after the last value in the linkedList if it is 1,2,3,4,5 -> then it was kept at 5 the whole time!)
0021. Merge Two Sorted Lists: Basically have a dummy = ListNode() because we can just simply return dummy.next -> its either going to be the start of the new linked list or it will be empty because both l1 and l2 are empty. also initialize tail = dummy as a pointer because then we can basically change the pointer as we go instead of changing the actual stuff within the pointer. -> basically while l1 and l2: if l1.val > l2.val: tail.next = l1, l1 = l1.next and else: tail.next = l2, l2 = l2.next then make sure to iterate tail = tail.next within the while loop. check at the end if l1: tail.next = l1 and elif l2: tail.next = l2. the reason we do this is because one of the lists may not be empty after the while loop. thus we can just append the start of the remaining part of one of the lists to the end of our dummy list. then simply return dummy.next (as dummy.next will either be the start of the list that has been merged, or it will be empty depending on whether l1 and l2 is empty)
0143. Reorder List: Simply find half of the list by doing slow = head, fast = head.next and then while fast and fast.next: fast = fast.next.next, slow = slow.next in order to find two halves of the list. The reason want to do this is because we want to reverse the second half of the list as we can then iterate backwards. To reverse the second half of the list, second = slow.next, slow.next = None in order to separate the two lists. Then do while second: tmp = second.next, second.next = prev, prev = second, second = tmp. Then in order to combine the two lists basically do second = prev because then it makes second point to the start of the reversed list. Then do while first and second: tmp1, tmp2 = first.next, second.next -> the reason we do this is in order to keep track of the current next pointers to iterate to the next values in both lists. Then we can do first.next = second, second = tmp1, then we can iterate first = tmp1, second = tmp2 -> that is the whole algorithm because we do not need to return this list, it simply exists due to dynamic allocation
0019. Remove Nth Node From End of List: Basically create a dummy node at the start of the list (return dummy.next) -> basically iterate l to be at dummy and r to be at head, iterate until there are n nodes between l and r -> while n > 0 and r: do r = r.next, n -= 1 then basically iterate until r until it reaches null -> while r: l = l.next, r = r.next then basically remove l.next by doing l.next = l.next.next -> because we iterated l from dummy node! the removed node is the l.next! return dummy.next
0138. Copy List with Random Pointer: Basically have two iterations, one where we create a deep copy where curr = head, while curr: (use a hashmap to map old to new deep copy) copy = Node(curr.val), oldToNew[curr] = copy (make sure to initialize oldToNew = { None : None } in order to map none to none -> no deep copy will be made if the original is one) curr = curr.next -> then second iteration update the pointers. The reason we have two iterations is because we need to create the deep copy nodes first in order to map them to each other. curr = head, while curr: copy = oldToNew[curr], copy.next = oldToNew[curr.next], copy.random = oldToNew[curr.random], curr = curr.next -> basically at the end return the deep copy head: return oldToNew[head]
0002. Add Two Numbers: dummy = ListNode() in order to start the return val with a dummy node so we can return dummy.next, curr = dummy have a pointer for the iteration. while l1 or l2 or carry: this is because we can basically make v1 null or v2 null depending on whether l1 or l2 is nullptr, but also we need to also continue it for or carry because 8 + 7 would give us a carry that we need to add, but we wouldn't be able to add it. then we do v1 = l1.val if l1 else 0, v2 = l2.val if l1 else 0, val = v1 + v2 + carry, then we must check if the val goes over 10 (essentially, is there a carry?) -> val %= 10 (as it gives us the remainder after // 10), carry = val // 10 (// is integer division, / is float division). then we can simply add curr.next = ListNode(val). Then we simply update the pointers for the next iteration: curr = curr.next, l1 = l1.next if l1 else None, l2 = l2.next if l2 else None -> basically making sure that if l1 is now done, then we make sure that l1 is returned as null because it would make v1 0 in the next iteration, while if l2 is finished, then it would be returned as nullptr: making v2 be 0 in the next iteration. However, if we do have a carry this while loop will continue. at the end, we can return dummy.next in order to return the start of the linked list (sum) -> using dummy node
0141. Linked List Cycle: Floyd's Hare and Tortoise algorithm -> basically have a slow and fast pointer -> slow = slow.next, fast = fast.next.next: do this while fast and fast.next: -> this is because is fast or fast.next -> null, this means that an "end" has been found. However, if a cycle exists, then it will never reach a nullptr.
0287. Find the Duplicate Number: Basically need to find the cycle first. The reason for this is because all the values in the array are going to be from 1->n-1 meaning that there will always be a cycle. The second step will be to find the duplicate number. This can be done by having two slow pointers (one starting at index 0, and the other one starting at where the cycle was found) -> this works because the distance from index 0 -> start of cycle and the distance from cycle detected index -> start of cycle will always be the same -> this is because of a mathematical proof regarding 2*slow = fast. Thus, since they must always go to the start of the cycle at some point (c-x) and p, they will be the same at one point. return slow or slow2, this doesn't matter since they will both be the same value (duplicate number at different indexes) -> they are pointing both to the index of the start of the cycle. 
0146. LRU Cache: Basically use a hashmap to access in O(1), but to access an "least recently used thing" -> use a linkedlist where the leftmost node and rightmost nodes (after the dummy nodes) as each side as a dummy node at the start and end to bypass the annoying edgecase that the linkedlist has no nodes at all -> left is LRU and right is MRU (least recently used, most recently used) -> create a list struct class ListNode: def __init__(self, key, value): self.key, self.val = key, value -> the reason we need a key and val data member for the listnode is to make sure we can access the hashmap from the linkedlist (for when we remove the LRU, we also need to remove it from the hashmap) -> make a def insert(self, node) and def remove(self, node) function inside class LRU to remove from linkedlist and to add from LinkedList. Insert basically adds it to right before the right dummy -> prev, next = self.right.prev, self.right -> node.next = next, node.prev = prev, prev.next = node, next.prev = node. for the remove, we are basically removing from the left of the linkedlist after the left dummy node -> prev, next = self.left, self.left.next, prev.next = node, next.prev = node, node.next = next, node.prev = prev
for each put and get, we must update the LRU linkedlist because then we have accessed a certain key. We can just remove it from the linkedlist and then re-insert it with the functions we made instead of trying to shift it. Shifting it in the linkedlist will be a pain in the ass, just remove it and then re-add it using the functions. 
0023. Merge k Sorted Lists: Basically have a helper function that merges two linkedlists. In the main function, check to see if lists and len(lists) == 0: then return None for that edge case. While len(lists) > 1: basically mergedLists = [] -> list so that we can maintain lists as it is. for i in range(0, len(lists), 2): (increment two at a time because of the merging idea) -> l1 = lists[i], l2 = lists[i + 1] if (i + 1) < len(lists) else None, then basically mergedLists.append(self.mergeList(l1, l2)) and then at the end basically make lists = mergedLists, and return lists[0].
0025. Reverse Nodes in k-Group: Basically have a helperfunct in ord to find the kth node from the currNode that we are on. -> this is simple as we can just do while currNode and k > 0: (in the helperfunct) -> currNode = currNode.next, k -= 1 --> then simply return currNode. The main function, we basically need to keep track of groupPrev and groupNext because we must update the pointers after we reverse the list (or the linkedlist will no longer be connected). To reverse, we must basically do prev, curr = kth.next, curr = groupPrev.next and then simply do while curr != groupNext: (not curr != None because we are reversing a group, not the entire linkedlist), then basically do temp = curr.next, curr.next = prev, prev = curr, curr = temp (basic reversal going on here) -> after the reversal to change the pointers around the group, we can simply do: temp = groupPrev.next (to keep a pointer to groupPrev.next before it gets updated as we need this to update the pointer after the group), groupPrev.next = kth (for the before node to point at the new head of the group), groupPrev = temp (temp still points to 1 (the head of the group before it got reversed) and we need to now make the groupPrev == the last value of the group in order to iterate to the next kth group iteration)


TREES: Sometimes must also keep track of more than 1 value in the recursion
0226. Invert Binary Tree: Can use pre-order or post-order for this, but I like to use post-order as it makes more sense to me. -> basically check the case if root is None because if it is, we can simply return None as the binarytree is empty. self.invertTree(root.left), self.invertTree(root.right), and then simply just do root.left, root.right = root.right, root.left and return root -> this does head recursion (backwards recursion) and it is very intuitive (post-order traversal)
0104. Maximum Depth of Binary Tree: Just simply have a base case for when root is nullptr: return 0, but in general return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
0543. Diameter of Binary Tree: Diameter does not count the currNode as + 1. It only gets the max of left height and right height. Thus we need to keep track of a diameter as a global function, and return the height. So basically since in Python we cannot directly pass something through another function by reference, we must make the function inside of itself. so we can do diameter = 0, but inside the dfs function, we can do nonlocal diameter -> which basically tells the dfs function that diameter has been declared outside as a global variable. Then we can basically do left = dfs(root.left), right = dfs(root.right), diameter = max(diameter, left + right), return 1 + max(left, right) -> for the height, but to also update the diameter. make sure the dfs function is before the call to dfs inside of the main solution function. after declaring the dfs function inside the main solution function before the call of itself (dfs function), simply call the dfs(root) and return diameter. 
0110. Balanced Binary Tree: Basically just use a dfs inside function and keep track of a bool to check balance and the height. -> this can be done by making the return val a list of [height, balanced] -> make sure to check left[1] and right[1] and abs(left[0] - right[0]) <= 1 for balanced. return [1 + max(left[0], right[0]), balanced] in order to return the height and the balanced bool
0100. Same Tree: Basically just use pre-order as we need to check and then iterate or else it would iterate in different speed -> whatever is recursively declared first would go all the way to the end first. first check if they are empty -> if not p and not q: return True, if p and q and p.val == q.val: return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right), else: return False.
0572. Subtree of Another Tree: Basically have a helperfunction that checks if the current passed in root is the start of the same subtree. In the main function, basically check if that is true by passing in root and subroot. else if it doesn't return true, we can check root.left and subroot and also root.right and subroot (we don't change subroot because we are only checking to see if the same subtree is within the main tree). Before that, we need some edge cases in which we can check if not subroot: always return True because regardless of whether root is null or not, if subroot is empty, it will always be valid. also check if not root: return False. This is because if the first statement didn't catch (meaning subroot is not empty), that means root is empty while subroot is not empty! This is not valid for obvious reasons.
0235. Lowest Common Ancestor of a Binary Search Tree: Basically we can check curr = root and whenever the split happens (where p goes to right and q goes to left subtree or vice versa, is where the common ancestor is! for obvious reasons. there can't be lower common ancestor because they went down different subtrees.) so basically check if curr.val > p.val and curr.val > q.val: make curr = curr.left, elif curr.val < p.val and curr.val < q.val: make curr = curr.right, else return curr -> basically check when the split occurs!
0102. Binary Tree Level Order Traversal: Basically do iterative BFS -> have a res, and use a q = collections.deque() and q.append(root) then while q: for i in range(len(q)): basically node = q.popleft() and check if node: level.append(node.val) q.append(node.left) q.append(node.right) and simply just do if level: res.append(level) -> outside of the while loop to basically see if level is not null or empty (just simply as a edge case) -> this is super easy, just simply BFS. 
0199. Binary Tree Right Side View: BFS level based iteration! Basically popleft() from the queue until q is empty (per level) -> this is because we need to get the rightmost node at each level! -> basically while q: rightSide = None, for i in range(len(q)): node = popleft(), if node: rightSide = node, q.append(node.left), q.append(node.right) and outside of the for loop -> basically do if rightSide: res.append(rightSide) -> then outside of the while, just simply return res. -> this is basically level based BFS making sure that we append the rightmost node at each step. 