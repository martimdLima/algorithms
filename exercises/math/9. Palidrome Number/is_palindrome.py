class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if 1 <= x <= 9:
            return True

        original_numeber = x
        reversed_number = 0

        while x > 0:
            last_digit = x % 10
            reversed_number = reversed_number * 10 + last_digit
            x = x // 10

        return reversed_number == original_numeber
