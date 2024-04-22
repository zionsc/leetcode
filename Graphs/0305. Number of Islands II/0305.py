class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def find(n):
            p=par[n]
            while(p!=par[p]):
                par[p]=par[par[p]]
                p=par[p]
            return p

        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if(p1==p2): return False
            if(rank[p1]>rank[p2]):
                par[p2]=p1
                rank[p1]+=1
            else:
                par[p1]=p2
                rank[p2]+=1
            return True

        res=[]
        par=defaultdict(lambda:None)
        rank=defaultdict(int)
        cnt=0
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        for position in positions:
            pos=tuple(position)
            r,c=position[0],position[1]
            if not par[pos]:
                par[pos]=pos
                rank[pos]=1
                cnt+=1
                for dr,dc in directions:
                    if r+dr in range(m) and c+dc in range(n) and par[(r+dr,c+dc)]:
                        if(union(pos,(r+dr,c+dc))):
                            cnt-=1
                        
            res.append(cnt)
        return res
            