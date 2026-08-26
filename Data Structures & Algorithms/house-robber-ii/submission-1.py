class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robber(values):
            rob1, rob2 = 0, 0
            for value in values:
                temp = max(rob1, rob2)
                rob1 = rob2 + value
                rob2 = temp
            return max(rob1, rob2)
        
        return max(robber(nums[:len(nums)-1]), robber(nums[1:]))
