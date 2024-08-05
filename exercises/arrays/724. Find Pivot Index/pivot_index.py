class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for idx, num in enumerate(nums):
            if sum(nums[:idx]) == sum(nums[idx + 1 :]):
                return idx

        return -1

    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for idx, num in enumerate(nums):
            if left_sum == (total_sum - left_sum - num):
                return idx
            left_sum += num

        return -1
