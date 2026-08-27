class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        cur = 0
        for num in nums:
            cur = max(num, cur + num)
            maximum = max(maximum, cur)
        return maximum