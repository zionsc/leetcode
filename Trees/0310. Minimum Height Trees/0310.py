class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        
        adjList=defaultdict(list)
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def bfs(node):
            q=deque([node])
            visited=set()
            visited.add(node)
            farthestNode=node
            parent=defaultdict(lambda:None)

            while(q):
                curr=q.popleft()
                for nei in adjList[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        farthestNode=nei
                        parent[nei]=curr
                        q.append(nei)
            return farthestNode, parent
        
        a,_=bfs(0)
        b,parent=bfs(a)

        path=[]
        while(b is not None):
            path.append(b)
            b=parent[b]
        
        mid=len(path)//2
        if(len(path)%2==0):
            return [path[mid-1],path[mid]]
        else:
            return [path[mid]]