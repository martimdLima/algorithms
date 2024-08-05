class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        end = len(nums) - 1
        nums.sort(reverse=True)

        if len(nums) == 3 and nums[1] + nums[2] > nums[0]:
            return nums[1] + nums[2] + nums[0]

        largest = 0
        i = 0
        while i + 2 <= end:
            a = nums[i + 1]
            b = nums[i]
            c = nums[i + 2]

            if a + c > b:
                return max(largest, (a + b + c))
            i += 1

        return largest


def largestPerimeter(nums: List[int]) -> int:
    nums.sort(reverse=True)

    for i in range(len(nums) - 2):
        if nums[i] < nums[i + 1] + nums[i + 2]:
            return nums[i] + nums[i + 1] + nums[i + 2]

    return 0
