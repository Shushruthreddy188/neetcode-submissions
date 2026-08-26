class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for total in range(1, n + 1):
            square = 1

            while square * square <= total:
                dp[total] = min(
                    dp[total],
                    1 + dp[total - square * square]
                )
                square += 1

        return dp[n]