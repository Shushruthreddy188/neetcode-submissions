import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = list(range(n))
        heapq.heapify(available)

        busy = []   # (endTime, room)
        count = [0] * n

        for start, end in meetings:
            duration = end - start

            # Free every room that is available by this meeting's start
            while busy and busy[0][0] <= start:
                endTime, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                # Use smallest-numbered free room
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))

            else:
                # No room available: delay the meeting
                endTime, room = heapq.heappop(busy)

                newEnd = endTime + duration

                heapq.heappush(busy, (newEnd, room))

            count[room] += 1

        return count.index(max(count))