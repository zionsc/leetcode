class Solution:

    def distance(self, x1,x2,y1,y2):
        return sqrt((x2-x1)**2 + (y2-y1)**2)

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj_list = defaultdict(set)
        for i in range(len(bombs)):
            x1,y1,r1 = bombs[i]
            for j in range(i, len(bombs)):
                x2,y2,r2 = bombs[j]
                one_two = self.distance(x1, x2, y1, y2)
                two_one = self.distance(x2, x1, y2, y1)
                if one_two <= r1:
                    adj_list[i].add(j)
                if two_one <= r2:
                    adj_list[j].add(i)
        
        def dfs(bomb):
            if bomb in self.visited:
                return
            self.num_bombs += 1
            self.res = max(self.res, self.num_bombs)
            self.visited.add(bomb)
            for next_bomb in adj_list[bomb]:
                dfs(next_bomb)

        self.res = 0
        self.visited = set()
        self.num_bombs = 0
        for i in range(len(adj_list)):
            dfs(i)
            self.num_bombs = 0
            self.visited.clear()
        return self.res
            
        

        

            