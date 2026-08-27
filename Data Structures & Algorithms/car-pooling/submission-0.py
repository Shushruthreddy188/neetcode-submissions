import heapq

class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])

        minHeap = []  # (end_location, passengers)
        currentPassengers = 0

        for passengers, start, end in trips:

            while minHeap and minHeap[0][0] <= start:
                endLocation, leavingPassengers = heapq.heappop(minHeap)
                currentPassengers -= leavingPassengers

            currentPassengers += passengers

            if currentPassengers > capacity:
                return False

            heapq.heappush(minHeap, (end, passengers))

        return True