class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1 and target > len(nums):
            return []

        nums.sort()

        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left, right = findFirst(nums, target), findLast(nums, target)

        if target not in nums:
            return []

        if right - left > 0:
            return [n for n in range(left, right + 1)]

        return [left, right] if left != right else [right]

    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []

        nums.sort()

        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left, right = findFirst(nums, target), findLast(nums, target)

        if (
            left <= right
            and left < len(nums)
            and nums[left] == target
            and nums[right] == target
        ):
            return list(range(left, right + 1))

        return []
