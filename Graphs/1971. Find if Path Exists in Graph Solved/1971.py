#benjamin420
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True

        adj_list=defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        q=deque([source])
        visited=set([source])
        while q:
            curr=q.popleft()
            for nei in adj_list[curr]:
                if nei==destination:
                    return True
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)

        return False
