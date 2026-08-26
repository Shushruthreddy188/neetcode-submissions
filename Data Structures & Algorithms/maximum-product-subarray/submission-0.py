class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax = nums[0]
        curMin = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            temp = curMax

            curMax = max(
                num,
                num * curMax,
                num * curMin
            )

            curMin = min(
                num,
                num * temp,
                num * curMin
            )

            res = max(res, curMax)

        return res