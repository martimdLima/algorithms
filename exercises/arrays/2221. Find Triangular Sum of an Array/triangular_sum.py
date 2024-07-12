class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        for n in range(1, len(nums), 1):
            tmp_result = nums[n - 1] + nums[n]
            if tmp_result >= 10:
                nums[n - 1] = tmp_result % 10
            else:
                nums[n - 1] = tmp_result

        return self.triangularSum(nums[:-1])

    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            for i in range(len(nums) - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            nums.pop()

        return nums[0]
