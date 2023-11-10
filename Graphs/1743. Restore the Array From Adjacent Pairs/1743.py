class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for val1, val2 in adjacentPairs:
            adj[val1].append(val2)
            adj[val2].append(val1)
            