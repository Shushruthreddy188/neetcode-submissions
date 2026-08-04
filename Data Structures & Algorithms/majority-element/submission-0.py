class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == maj:
                count += 1
            elif count > 0 and nums[i] != maj:
                count -= 1
            else:
                maj = nums[i]
                count = 1
        return maj