class Solution:
    def countOdds(self, low: int, high: int) -> int:
        starting_point = low % 2  # Adjust low to the nearest odd number if it's even

        if starting_point == 0:
            low += 1

        num_count = high - low + 1  # total count of integers in the range.
        num_odds = (num_count + 1) // 2

        return num_odds
