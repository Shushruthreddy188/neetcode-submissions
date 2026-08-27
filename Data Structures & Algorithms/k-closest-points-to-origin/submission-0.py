import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []

        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(heap, (dist, x, y))

        res = []

        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])

        return res