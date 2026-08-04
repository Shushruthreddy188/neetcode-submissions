class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        concat_nums = [1]* (n * 2)
        for i, num in enumerate(nums):
            concat_nums[i] = concat_nums[i + n] = num
        return concat_nums
