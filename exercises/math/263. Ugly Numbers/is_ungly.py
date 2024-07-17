class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        primes = [2, 3, 5]
        p_counter = 0
        while n >= 1:
            if p_counter > 2:
                return False

            if n % primes[p_counter] == 0:
                n = n // primes[p_counter]
                continue

            p_counter += 1

        return n == 1
