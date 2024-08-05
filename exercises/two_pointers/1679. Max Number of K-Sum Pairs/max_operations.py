class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1
        max_operations = 0

        while left < right:
            k_sum = nums[left] + nums[right]

            if k_sum == k:
                max_operations += 1
                left += 1
                right -= 1
            elif k_sum > k:
                right -= 1
            else:
                left += 1

        return max_operations
