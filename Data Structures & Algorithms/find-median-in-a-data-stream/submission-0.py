import heapq

class MedianFinder:

    def __init__(self):
        self.left = []   # max heap (store negatives)
        self.right = []  # min heap

    def addNum(self, num: int) -> None:
        # Add to left half
        heapq.heappush(self.left, -num)

        # Ensure every left value <= every right value
        heapq.heappush(self.right, -heapq.heappop(self.left))

        # Keep left at least as large as right
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]

        return (-self.left[0] + self.right[0]) / 2.0