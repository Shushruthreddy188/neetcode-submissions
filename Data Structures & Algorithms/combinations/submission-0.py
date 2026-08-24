class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        cur = []

        def backtrack(start):
            # We picked k numbers
            if len(cur) == k:
                res.append(cur.copy())
                return

            for num in range(start, n + 1):
                # Choose
                cur.append(num)

                # Explore
                backtrack(num + 1)

                # Undo
                cur.pop()

        backtrack(1)
        return res