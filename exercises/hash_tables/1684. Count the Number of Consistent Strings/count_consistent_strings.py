class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent_strings_counter = 0

        allowed_counter = Counter(allowed)

        for word in words:
            word_counter = Counter(word)

            if allowed_counter.keys() == word_counter.keys() or word_counter.keys() <= allowed_counter.keys():
                consistent_strings_counter += 1

        return consistent_strings_counter

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        consistent_strings_counter = 0

        for word in words:
            if all(char in allowed_set for char in word):
                consistent_strings_counter += 1

        return consistent_strings_counter
