class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for nei in graph[node]:
                dfs(nei)

        components = 0

        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)

        return components