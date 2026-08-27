from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks)

        maxHeap = [-freq for freq in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        queue = []  # [freq, available_time]

        while maxHeap or queue:
            time += 1

            if maxHeap:
                freq = 1 + heapq.heappop(maxHeap)

                if freq != 0:
                    queue.append([freq, time + n])

            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.pop(0)[0])

        return time