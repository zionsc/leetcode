class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        adj_list = defaultdict(set)
        for i in range(len(paths)):
            src, dst = paths[i]
            adj_list[src].add(dst)
        
        for i in range(len(paths)):
            city1, city2 = paths[i]
            if len(adj_list[city1]) == 0:
                return city1
            elif len(adj_list[city2]) == 0:
                return city2
            