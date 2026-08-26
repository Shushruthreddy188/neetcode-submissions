class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        min_effort = [[float("inf")] * cols for _ in range(rows)]
        min_effort[0][0] = 0

        min_heap = [(0, 0, 0)]  # effort, row, col

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while min_heap:
            effort, r, c = heapq.heappop(min_heap)

            if r == rows - 1 and c == cols - 1:
                return effort

            if effort > min_effort[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    diff = abs(heights[nr][nc] - heights[r][c])

                    new_effort = max(effort, diff)

                    if new_effort < min_effort[nr][nc]:
                        min_effort[nr][nc] = new_effort
                        heapq.heappush(
                            min_heap,
                            (new_effort, nr, nc)
                        )

        return 0