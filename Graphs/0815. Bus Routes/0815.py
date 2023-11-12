class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        max_stop = max(max(route) for route in routes)
        if max_stop < target:
            return -1

        n = len(routes)
        min_buses_to_reach = [float('inf')] * (max_stop + 1)
        min_buses_to_reach[source] = 0

        flag = True
        while flag:
            flag = False
            for route in routes:
                mini = float('inf')
                for stop in route:
                    mini = min(mini, min_buses_to_reach[stop])
                mini += 1
                for stop in route:
                    if min_buses_to_reach[stop] > mini:
                        min_buses_to_reach[stop] = mini
                        flag = True

        return min_buses_to_reach[target] if min_buses_to_reach[target] < float('inf') else -1
        # if source == target:
        #     return 0

        # stop_to_route = defaultdict(set)
        # for route_id, route in enumerate(routes):
        #     for stop in route:
        #         stop_to_route[stop].add(route_id)

        # adj_graph = defaultdict(set)
        # for route_id, stops in enumerate(routes):
        #     for stop in stops:
        #         for nei in stop_to_route[stop]:
        #             if nei != route_id:
        #                 adj_graph[route_id].add(nei)

        # visited = set()
        # queue = deque()

        # for route_id in stop_to_route[source]:
        #     if target in routes[route_id]:
        #         return 1
        #     queue.append((route_id, 1))
        #     visited.add(route_id)

        # while queue:
        #     route_id, num_buses = queue.popleft()
        #     for nei_id in adj_graph[route_id]:
        #         if nei_id not in visited:
        #             visited.add(nei_id)
        #             if target in routes[nei_id]:
        #                 return num_buses + 1
        #             queue.append((nei_id, num_buses + 1))

        # return -1
