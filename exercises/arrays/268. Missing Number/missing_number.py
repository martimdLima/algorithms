class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_num = [n for n in range(0, len(nums) + 1) if n not in nums]
        return 0 if not missing_num else missing_num[0]

    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
