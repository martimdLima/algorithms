class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        return True if len([n for n in nums if n % 2 == 0]) >= 2 else False
