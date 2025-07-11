import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        counts = [0] * n
        rooms = list(range(n))
        bookings = []
        meetings.sort()
        for start,end in meetings:
            while bookings and bookings[0][0] <= start:
                e, room = heapq.heappop(bookings)
                heapq.heappush(rooms, room)
            if not rooms:
                e, room = heapq.heappop(bookings)
                heapq.heappush(bookings, (e + end - start, room))
                counts[room] += 1
            else:
                room = heapq.heappop(rooms)
                heapq.heappush(bookings, (end, room))
                counts[room] += 1
        maxv = max(counts)
        for i,v in enumerate(counts):
            if v == maxv:
                return i
        return -1
