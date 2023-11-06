class SeatManager:

    def __init__(self, n: int):
        self.seats = [i for i in range(1, n + 1)]
        heapq.heapify(self.seats)

    def reserve(self) -> int:
        seat = heapq.heappop(self.seats)
        return seat

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)
        

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)