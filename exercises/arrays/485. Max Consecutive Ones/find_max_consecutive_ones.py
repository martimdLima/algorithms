class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        current_count = 0
        max_consecutive_ones = 0

        for num in nums:
            if num == 1:
                current_count += 1
            else:
                max_consecutive_ones = max(max_consecutive_ones, current_count)
                current_count = 0

        return max(max_consecutive_ones, current_count)
