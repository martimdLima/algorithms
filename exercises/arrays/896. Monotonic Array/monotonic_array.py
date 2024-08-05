class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True

        increasing = decreasing = True

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False
            if nums[i] < nums[i - 1]:
                increasing = False

            if not increasing and not decreasing:
                return False

        return increasing or decreasing
