# #benjamin420
# class Solution:
#     def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
#         if source==destination:
#             return True

#         adj_list=defaultdict(list)
#         for u,v in edges:
#             adj_list[u].append(v)
#             adj_list[v].append(u)
        
#         q=deque([source])
#         visited=set([source])
#         while q:
#             curr=q.popleft()
#             for nei in adj_list[curr]:
#                 if nei==destination:
#                     return True
#                 if nei not in visited:
#                     q.append(nei)
#                     visited.add(nei)

#         return False


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        par=[i for i in range(n)]
        rank=[1] * n

        def find(node):
            p=par[node]
            while p!=par[p]:
                par[p]=par[par[p]]
                p=par[p]
            return p
        
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return True
            if rank[p1]>rank[p2]:
                par[p2]=p1
                rank[p1]+=rank[p2]
            else:
                par[p1]=p2
                rank[p2]+=rank[p1]

        for n1,n2 in edges:
            union(n1,n2)
            
        return find(source)==find(destination)