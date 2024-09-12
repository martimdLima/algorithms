from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        word1_counter = Counter(word1)
        word2_counter = Counter(word2)

        word1_keys = list(word1_counter.keys())
        word1_values = list(word1_counter.values())
        word1_keys.sort()
        word1_values.sort()

        word2_keys = list(word2_counter.keys())
        word2_values = list(word2_counter.values())
        word2_keys.sort()
        word2_values.sort()

        if word1_keys == word2_keys and word1_values == word2_values:
            return True
        else:
            return False

        return False

    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        word1_counter = Counter(word1)
        word2_counter = Counter(word2)

        # Check if the sets of unique characters are the same
        if set(word1_counter.keys()) != set(word2_counter.keys()):
            return False

        # Check if the sorted frequency values are the same
        if sorted(word1_counter.values()) != sorted(word2_counter.values()):
            return False

        return True
