class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []

        left_products = [1] * n
        right_products = [1] * n

        # left_products will hold the product of all elements to the left of index i
        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]

        # right_products will hold the product of all elements to the left of index i
        for i in range(n - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]

        # Construct the result
        results = [left_products[i] * right_products[i] for i in range(n)]

        return results
