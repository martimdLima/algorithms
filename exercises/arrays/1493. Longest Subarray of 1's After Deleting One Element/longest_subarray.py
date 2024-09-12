from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        right = [0] * n

        if nums.count(1) == 0:
            return 0

        for i in range(1, n - 1):
            if nums[i - 1] == 1:
                left[i] = left[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if nums[i + 1] == 1:
                right[i] = right[i + 1] + 1

        result = [left[idx] + right[idx] for idx in range(0, len(left) - 1)]

        return 0 if len(result) == 0 else max(result)
