class Solution:
    def climbStairs(self, n: int) -> int:
        n1, n2 = 1, 1
        for i in range(1,n):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2