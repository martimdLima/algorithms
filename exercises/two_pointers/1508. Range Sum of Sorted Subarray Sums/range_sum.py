class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        length = len(nums)
        sums = []

        for i in range(length):
            current_sum = 0
            for x in range(i, length):
                current_sum += nums[x]
                sums.append(current_sum)

        sums.sort()

        mod = 10**9 + 7

        return sum(sums[left - 1 : right]) % mod
