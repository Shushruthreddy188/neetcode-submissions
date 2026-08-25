class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []

        def backtrack():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for num in nums:
                if num in perm:
                    continue

                perm.append(num)

                backtrack()

                perm.pop()

        backtrack()
        return res