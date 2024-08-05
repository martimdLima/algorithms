class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        max_vowels = 0
        current_vowels = 0

        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
        max_vowels = current_vowels

        for i in range(k, len(s)):
            # Remove the effect of the character that goes out of the window
            if s[i - k] in vowels:
                current_vowels -= 1
            # Add the effect of the character that comes into the window
            if s[i] in vowels:
                current_vowels += 1

            max_vowels = max(max_vowels, current_vowels)
        return max_vowels
