class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_first, right_first = 0, len(nums) - 1
        left_last, right_last = 0, len(nums) - 1

        while left_first <= right_first:
            mid = left_first + (right_first - left_first) // 2
            if nums[mid] >= target:
                right_first = mid - 1
            else:
                left_first = mid + 1

        while left_last <= right_last:
            mid = left_last + (right_last - left_last) // 2
            if nums[mid] <= target:
                left_last = mid + 1
            else:
                right_last = mid - 1

        if (
            left_first <= right_last
            and left_first < len(nums)
            and nums[left_first] == target
            and nums[right_last] == target
        ):
            return [left_first, right_last]

        return [-1, -1]
