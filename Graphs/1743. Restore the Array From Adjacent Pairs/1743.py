class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for val1, val2 in adjacentPairs:
            adj[val1].append(val2)
            adj[val2].append(val1)
        
        start_node = None
        for i, v in adj.items():
            if len(v) == 1:
                start_node = i
                break
        