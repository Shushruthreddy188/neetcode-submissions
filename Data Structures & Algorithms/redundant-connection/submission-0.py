class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = [[] for _ in range(n + 1)]

        def dfs(node, target, visited):
            if node == target:
                return True

            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True

            return False

        for a, b in edges:
            # If a can already reach b, adding a-b creates a cycle
            if graph[a] and graph[b] and dfs(a, b, set()):
                return [a, b]

            graph[a].append(b)
            graph[b].append(a)

        return []