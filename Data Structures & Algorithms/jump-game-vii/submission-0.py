class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        dp = [False] * n
        dp[0] = True

        reachable = 0

        for i in range(1, n):
            if i - minJump >= 0:
                reachable += dp[i - minJump]

            if i - maxJump - 1 >= 0:
                reachable -= dp[i - maxJump - 1]

            dp[i] = s[i] == '0' and reachable > 0

        return dp[-1]