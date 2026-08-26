class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        minHeap = [(0, k)]  # distance, node
        visited = set()

        max_time = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)
            max_time = max(max_time, time)

            for nei, weight in graph[node]:
                if nei not in visited:
                    heapq.heappush(
                        minHeap,
                        (time + weight, nei)
                    )

        return max_time if len(visited) == n else -1