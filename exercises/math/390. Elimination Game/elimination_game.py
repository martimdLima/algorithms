class Solution:
    def lastRemaining(self, n: int) -> int:
        last = 1
        step = 1
        left = True  # Start from left side

        while n > 1:
            if left or n % 2 == 1:
                last += step
            n //= 2
            step *= 2
            left = not left

        return last
