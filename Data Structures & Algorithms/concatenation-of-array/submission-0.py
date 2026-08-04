class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        concat_nums = [1]*len(nums) * 2
        for i in range(len(nums)):
            concat_nums[i] = concat_nums[i + len(nums)] = nums[i]
        return concat_nums
