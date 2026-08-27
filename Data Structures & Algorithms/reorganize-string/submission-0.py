from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        maxHeap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(maxHeap)

        res = []
        prev = None

        while maxHeap:
            freq, char = heapq.heappop(maxHeap)

            res.append(char)
            freq += 1

            if prev:
                heapq.heappush(maxHeap, prev)

            if freq != 0:
                prev = (freq, char)
            else:
                prev = None

        if prev:
            return ""

        return "".join(res)