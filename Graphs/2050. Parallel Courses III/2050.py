class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # adj list
        adj_list = defaultdict(list)
        in_degree = [0] * (n + 1)

        for preq, crs in relations:
            adj_list[preq].append(crs)
            in_degree[crs] += 1

        queue = deque()

        for i in range(1, n + 1):
            if in_degree[i] == 0:
                queue.append(i)

        topo_order = []

        while queue:
            crs = queue.pop()
            topo_order.append(crs)
            for nei in adj_list[crs]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)

            


        