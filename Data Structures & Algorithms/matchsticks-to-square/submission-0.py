class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        target = total // 4

        matchsticks.sort(reverse=True)

        sides = [0, 0, 0, 0]

        def backtrack(i):
            if i == len(matchsticks):
                return True

            for j in range(4):
                if sides[j] + matchsticks[i] <= target:
                    sides[j] += matchsticks[i]

                    if backtrack(i + 1):
                        return True

                    sides[j] -= matchsticks[i]

            return False

        return backtrack(0)