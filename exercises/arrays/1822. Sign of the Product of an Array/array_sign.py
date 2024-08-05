class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0

        return 1 if math.prod(nums) > 0 else -1
