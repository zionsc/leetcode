class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set=set(deadends)
        if "0000" in dead_set:
            return -1
        
        def next_step(code):
            for i in range(4):
                x=int(code[i])
                for d in (-1,1):
                    y=(x+d)%10
                    yield code[:i]+str(y)+code[i+1:]
        
        q=deque([("0000",0)])
        visited=set(["0000"])

        while q:
            code,steps=q.popleft()
            if steps==target:
                return steps
            for next_code in next_step(code):
                if next_code not in visited and next_code not in dead_set:
                    visited.add(next_code)
                    q.append((next_code,steps+1))

        return -1