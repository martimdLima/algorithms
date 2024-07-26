class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)

        for idx, candie in enumerate(candies):
            is_greater = True if candie + extraCandies >= greatest else False
            candies[idx] = is_greater

        return candies
