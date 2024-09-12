class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        zero_count = 0
        max_consecutive_ones = 0

        if k >= nums.count(0):
            return len(nums)

        for right in range(n):
            # Expand the window by including nums[right]
            if nums[right] == 0:
                zero_count += 1

            # Check and maintain the window with at most k zeros
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            if zero_count == k:
                max_consecutive_ones = max(max_consecutive_ones, len(nums[left : right + 1]))

        return max_consecutive_ones

    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_consecutive_ones = 0

        for right in range(len(nums)):
            # Expand the window by including nums[right]
            if nums[right] == 0:
                zero_count += 1

            # Check and maintain the window with at most k zeros
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Calculate the length of the current valid window
            max_consecutive_ones = max(max_consecutive_ones, right - left + 1)

        return max_consecutive_ones
