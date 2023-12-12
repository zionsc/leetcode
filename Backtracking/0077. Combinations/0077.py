class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # res = list(range(1,n + 1))
        # return list(combinations(res, k))

        res = set()
        
        def backtrack(first, temp):
            if len(temp) == k:
                if tuple(temp) not in res:
                    res.add(tuple(temp.copy()))
                return
            
            for i in range(first, n + 1):
                temp.append(i)
                backtrack(i + 1, temp)
                temp.pop()
        
        backtrack(1, [])
        return res


