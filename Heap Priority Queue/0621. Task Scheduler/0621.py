class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # basically gives me a hashmap [character, number of occurences within tasks]
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count] # this is how you create maxheaps in python! --> no library maxheap function
        heapq.heapify(maxHeap)
        q = deque() # in order to keep track of tasks that are idle, but still need to be completed

        time = 0

        # means that there are still tasks to be completed 
        while maxHeap or q:
            time += 1
            if maxHeap:
                # we do + 1 here because the values are negated, 
                # meaning they are negative. (we want to decrease the value by 1 since we are processing it in the CPU)
                cnt = 1 + heapq.heappop(maxHeap) 

                if cnt: # if cnt != 0
                    # reason we do time + n is because we are making sure we remove the value and add it back to the maxheap when the time that it is not idle!
                    q.append([cnt, time + n]) 
            if q and q[0][1] == time: # earliest item to be added to the q's time is == to the time it is no longer idle
                heapq.heappop(maxHeap, q.popleft()[0]) # we do q.popleft()[0] because we want the count, not the time.

        return time