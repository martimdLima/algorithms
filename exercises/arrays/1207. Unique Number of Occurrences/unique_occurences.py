class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique_occurences = Counter(arr)

        unique_occurences_values = unique_occurences.values()

        return len(unique_occurences_values) == len(set(unique_occurences_values))
