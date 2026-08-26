class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        if obstacleGrid[0][0] == 1:
            return 0

        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                    continue

                if r == 0 and c == 0:
                    continue

                top = dp[r - 1][c] if r > 0 else 0
                left = dp[r][c - 1] if c > 0 else 0

                dp[r][c] = top + left

        return dp[m - 1][n - 1]