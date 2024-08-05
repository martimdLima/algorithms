class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) < 2:
            return True

        arr.sort()

        element = 1
        diff = arr[1] - arr[0]
        while element + 1 <= len(arr) - 1:
            current_diff = arr[element + 1] - arr[element]
            if current_diff != diff:
                return False
            element += 1
        return True

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) < 2:
            return True

        min_val = min(arr)
        max_val = max(arr)
        n = len(arr)

        # If the difference between min and max values is not divisible by n-1,
        # it cannot be an arithmetic progression.
        if (max_val - min_val) % (n - 1) != 0:
            return False

        diff = (max_val - min_val) // (n - 1)

        # Create a set for all the values that should be in the arithmetic progression
        expected_values = set(min_val + i * diff for i in range(n))

        # Check if the set of the given array matches the expected values
        return set(arr) == expected_values
