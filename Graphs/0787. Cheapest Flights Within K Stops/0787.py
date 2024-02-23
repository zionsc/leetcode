class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # creating the adjacency list
        adj_list = defaultdict(list)
        for f,t,p in flights:
            adj_list[f].append([t,p])

        # kept as res but also to stop if iteration ever larger than before cache
        prices = [float('inf')] * n
        prices[src] = 0

        queue = deque([(0,src,0)]) # price, node, steps

        while queue:
            curr_price, curr_node, curr_steps = queue.popleft()
            for nei_node,nei_price in adj_list[curr_node]:
                if curr_price + nei_price < prices[nei_node] and curr_steps <= k:
                    prices[nei_node] = curr_price + nei_price
                    queue.append((curr_price + nei_price, nei_node, curr_steps + 1))
        
        return prices[dst] if prices[dst] != float('inf') else -1