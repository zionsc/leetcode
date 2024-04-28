class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList=defaultdict(list)
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        res=[0]*n
        count=[1]*n

        def dfs1(node, parent):
            for child in adjList[node]:
                if child!=parent:
                    dfs1(child,node)
                    count[node]+=count[child]
                    res[node]+=res[child]+count[child]
        
        def dfs2(node,parent):
            for child in adjList[node]:
                if child!=parent:
                    res[child]=res[node]-count[child]+(n-count[child])
                    dfs2(child,node)
        
        return res