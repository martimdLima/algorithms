class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and target > nums[0]:
            return 1
        elif len(nums) == 1 and target < nums[0]:
            return 0

        if target in nums:
            return nums.index(target)

        left = 0
        right = len(nums) - 1

        while left <= right:
            if target < nums[left]:
                return (
                    0
                    if (nums.index(nums[left]) - 1) < 0
                    else nums.index(nums[left]) - 1
                )

            if target > nums[left] and target < nums[left + 1]:
                return nums.index(nums[left]) + 1

            if target > nums[right]:
                return nums.index(nums[right]) + 1

            if target < nums[right] and target > nums[right] - 1:
                return (
                    0
                    if (nums.index(nums[right]) - 1) < 0
                    else nums.index(nums[right]) - 1
                )
            left += 1
            right -= 1

        return 0
