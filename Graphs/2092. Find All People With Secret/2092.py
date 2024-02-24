class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        res = set([0, firstPerson])
        time_map = {} # time : adj_list[x]:y
        for x,y,t in meetings:
            if t not in time_map:
                time_map[t] = defaultdict(list)
            time_map[t][x].append(y)
            time_map[t][y].append(x)
        
        def dfs(src, adj_list):
            if src in visited:
                return
            visited.add(src)
            res.add(src)
            for nei in adj_list[src]:
                dfs(nei, adj_list)

        for t in sorted(time_map.keys()):
            visited = set()
            for src in time_map[t]:
                if src in res:
                    dfs(src, time_map[t])
        
        return list(res)
