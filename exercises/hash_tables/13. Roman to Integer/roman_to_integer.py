class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        result = 0
        previous = 0

        for char in s[::-1]:
            if roman_to_int_dict.get(char) >= previous:
                result += roman_to_int_dict.get(char)
            else:
                result -= roman_to_int_dict.get(char)
            previous = roman_to_int_dict.get(char)

        return result
