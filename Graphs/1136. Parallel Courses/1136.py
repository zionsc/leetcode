class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for pre,crs in relations:
            adj_list[crs].append(pre)

        visited = defaultdict(int)

        def dfs(crs: int) -> int:
            if crs in visited:
                return visited[crs]
            else:
                visited[crs] = -1
            
            max_length = 1 # beacuse current is also a length
            for pre in adj_list[crs]:
                length = dfs(pre)
                if length == -1:
                    return -1
                else:
                    max_length = max(max_length, length + 1)
            visited[crs] = max_length
            return max_length
        
        res = 0
        for crs in range(1, n + 1):
            length = dfs(crs)
            if length == -1:
                return -1
            else:
                res = max(res, length)
        return res