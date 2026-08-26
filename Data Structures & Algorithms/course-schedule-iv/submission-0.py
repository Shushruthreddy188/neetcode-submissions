class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]]
    ) -> List[bool]:

        graph = [[] for _ in range(numCourses)]

        for prereq, course in prerequisites:
            graph[prereq].append(course)

        def dfs(course, target, visited):
            if course == target:
                return True

            if course in visited:
                return False

            visited.add(course)

            for nei in graph[course]:
                if dfs(nei, target, visited):
                    return True

            return False

        res = []

        for prereq, course in queries:
            res.append(dfs(prereq, course, set()))

        return res