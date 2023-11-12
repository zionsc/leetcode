class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # Build a graph where each stop is associated with the buses that pass through it
        stop_to_buses = defaultdict(list)

        for bus_id, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(bus_id)

        # Check if source and target stops are in the graph
        if source not in stop_to_buses or target not in stop_to_buses:
            return -1

        # If the source and target are the same stop, no buses are needed
        if source == target:
            return 0

        # Use BFS to find the minimum number of buses to reach the target stop
        queue = deque([source])
        buses_taken = set()
        stops_visited = set()
        res = 0

        while queue:
            # Increment the res for each level of stops
            res += 1
            stops_to_process = len(queue)

            for _ in range(stops_to_process):
                current_stop = queue.popleft()

                # Check buses passing through the current stop
                for bus_id in stop_to_buses[current_stop]:
                    if bus_id in buses_taken:
                        continue

                    buses_taken.add(bus_id)

                    # Check stops reachable from the current bus
                    for next_stop in routes[bus_id]:
                        if next_stop in stops_visited:
                            continue

                        # If the target is reached, return the res
                        if next_stop == target:
                            return res

                        # Add the next stop to the queue and mark it as visited
                        queue.append(next_stop)
                        stops_visited.add(next_stop)

        # If no valid route is found
        return -1
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
