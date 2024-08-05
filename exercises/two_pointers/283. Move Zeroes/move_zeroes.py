class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if 0 not in nums:
            return nums

        counter = 0
        start = 0

        while start <= len(nums) - 1:
            if nums[start] == 0:
                nums.pop(start)
                counter += 1
            else:
                start += 1
                continue

        for ele in range(0, counter):
            nums.append(0)

    def moveZeroes(self, nums: List[int]) -> None:
        next_non_zero = 0
        
        for current in range(len(nums)):
            if nums[current] != 0:
                nums[next_non_zero], nums[current] = nums[current], nums[next_non_zero]
                next_non_zero += 1