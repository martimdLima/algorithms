class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left = float("inf")
        mid = float("inf")

        for idx, num in enumerate(nums):
            if mid < num:
                return True
            elif num <= left:
                left = num
            elif left < num < mid:
                mid = num

        return False
