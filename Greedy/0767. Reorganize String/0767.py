class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s) 
        max_heap = []
        res = []
        for c,f in count.items():
            heapq.heappush(max_heap, (-f, c))
        
        while max_heap:
            f1, c1 = heapq.heappop(max_heap)
            if max_heap:
                f2, c2 = heapq.heappop(max_heap)
                res.append(c1)
                res.append(c2)
                if f2 + 1 != 0:
                    heapq.heappush(max_heap, (f2 + 1, c2))
            else:
                res.append(c1)

            if len(res) > 1 and res[-1] == res[-2]:
                return ""
            if f1 + 1 != 0:
                heapq.heappush(max_heap, (f1 + 1, c1))
            
            
        return "".join(res)
        
        



