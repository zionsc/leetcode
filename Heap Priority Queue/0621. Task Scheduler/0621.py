class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # basically gives me a hashmap [character, number of occurences within tasks]
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count] # this is how you create maxheaps in python! --> no library maxheap function
        heapq.heapify(maxHeap)
        q = deque() # in order to keep track of tasks that are idle, but still need to be completed

        time = 0

        while maxHeap