class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:(x[0])) # sort meetings by start time
        room_freq = [0] * n
        free_rooms = [i for i in range(n)]
        end_information = [] # (end_time, room)
        heapq.heapify(free_rooms)
        room_res, num_res = 0,0

        for start,end in meetings:
            while end_information and end_information[0][0] <= start:
                end_time, next_room = heapq.heappop(end_information)
                heapq.heappush(free_rooms, next_room)
            if free_rooms:
                used_room = heapq.heappop(free_rooms)
                heapq.heappush(end_information, [end, used_room])
                room_freq[used_room] += 1
            else:
                end_time, next_room = heapq.heappop(end_information)
                if start < end_time:
                    delayed_end = (end - start) + end_time
                    heapq.heappush(end_information, [delayed_end, next_room])
                else:
                    heapq.heappush(end_information, [end, next_room])
                room_freq[next_room] += 1


        for i,v in enumerate(room_freq):
            if v > num_res:
                room_res = i
                num_res = v

        return room_res