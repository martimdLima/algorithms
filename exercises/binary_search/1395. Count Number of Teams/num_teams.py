class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def build(self, data):
        for i in range(len(data)):
            self.update(i + 1, data[i])

    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        result = 0
        while index:
            result += self.tree[index]
            index -= index & -index
        return result

    def range_query(self, left, right):
        return self.prefix_sum(right) - self.prefix_sum(left - 1)


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def binary_search(arr, x):
            low = 0
            high = len(arr) - 1
            mid = 0

            while low <= high:
                mid = (high + low) // 2

                if arr[mid] < x:
                    low = mid + 1
                elif arr[mid] > x:
                    high = mid - 1
                else:
                    return mid

            return -1

        # Sort and remove duplicates
        sorted_ratings = sorted(set(rating))
        sorted_ratings_size = len(sorted_ratings)

        # Initialize Trees
        tree_smaller = FenwickTree(sorted_ratings_size)
        tree_greater = FenwickTree(sorted_ratings_size)

        # Populate greater tree with the count of each rating
        for value in rating:
            index = binary_search(sorted_ratings, value) + 1
            tree_greater.update(index, 1)

        num_soldiers = len(rating)
        result = 0

        for idx, value in enumerate(rating):
            index = binary_search(sorted_ratings, value) + 1

            # Update the trees
            tree_smaller.update(index, 1)
            tree_greater.update(index, -1)

            # Find l (left count) and r (right count)
            left_smaller = tree_smaller.query(index - 1)
            right_greater = num_soldiers - idx - 1 - tree_greater.query(index)

            # Accumulate the number of teams possible with the current soldier
            result += left_smaller * right_greater
            result += (idx - left_smaller) * (num_soldiers - idx - 1 - right_greater)

        return result
