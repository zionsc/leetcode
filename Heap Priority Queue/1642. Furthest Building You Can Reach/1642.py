class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                if len(min_heap) < ladders:
                    heapq.heappush(min_heap, diff)
                else:
                    min_diff = heapq.heappushpop(min_heap, diff)
                    if bricks >= min_diff:
                        bricks -= min_diff
                    else:
                        return i
        return len(heights) - 1