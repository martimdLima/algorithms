class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]

        current_average = sum(nums[:k])
        max_average = current_average

        for idx in range(k, len(nums)):
            current_average += nums[idx] - nums[idx - k]
            max_average = max(max_average, current_average)

        return max_average / k
