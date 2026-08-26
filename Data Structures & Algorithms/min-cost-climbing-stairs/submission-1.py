class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1,prev2 = 0,0

        for c in cost:
            prev1,prev2 = prev2,c+min(prev1,prev2)

        return min(prev1,prev2)