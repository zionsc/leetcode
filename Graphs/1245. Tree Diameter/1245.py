class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        def dfs(node, prev):
            longest_path = 0
            for nei in adj_list[node]:
                if nei == node:
                    continue
                curr_path = 1 + dfs(nei, node)
                self.diameter = max(self.diameter, longest_path + curr_path)
                longest_path = max(longest_path, curr_path)
            return longest_path
        
        self.diameter = 0
        dfs(0, -1)
        return self.diameter