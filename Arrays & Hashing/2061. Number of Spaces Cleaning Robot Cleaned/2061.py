class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        row,col=len(room),len(room[0])
        visited=set()
        res=r=c=curr=0
        while (r,c,curr) not in visited:
            visited.add((r,c,curr))
            if room[r][c]==0:
                room[r][c]=-1
                res+=1
            if 0<=r+directions[curr][0]<row and 0<=c+directions[curr][1]<col and room[r+directions[curr][0]][c+directions[curr][1]]!=1:
                r+=directions[curr][0]
                c+=directions[curr][1]
            else:
                curr=(curr+1)%4
        return res
