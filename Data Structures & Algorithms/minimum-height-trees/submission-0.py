class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = [[] for _ in range(n)]
        degree = [0] * n

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1

        q = deque()

        for node in range(n):
            if degree[node] == 1:
                q.append(node)

        remaining = n

        while remaining > 2:
            leaves = len(q)
            remaining -= leaves

            for _ in range(leaves):
                leaf = q.popleft()

                for nei in graph[leaf]:
                    degree[nei] -= 1

                    if degree[nei] == 1:
                        q.append(nei)

        return list(q)