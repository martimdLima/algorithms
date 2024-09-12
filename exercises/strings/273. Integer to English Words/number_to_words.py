class Solution:
    def numberToWords(self, num: int) -> str:
        # Define mappings for numbers to words
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = [
            "",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion", "Trillion"]

        def three_digit_number_to_words(n):
            if n == 0:
                return ""
            elif n < 10:
                return ones[n]
            elif 10 < n < 20:
                return teens[n - 10]
            elif n < 100:
                return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
            else:
                return (
                    ones[n // 100] + " Hundred" + (" " + three_digit_number_to_words(n % 100) if n % 100 != 0 else "")
                )

        def int_to_str(num, num_len, units_val, words):
            if num == 0:
                return "Zero"

            num_str = str(num)

            if num_len > 0:
                three_digits = int(num_str[max(0, num_len - 3) : num_len])
                if three_digits:
                    words.append(f"{three_digit_number_to_words(three_digits)} {thousands[units_val]}")
            else:
                return " ".join(list(reversed(words))).rstrip()

            num_len -= 3
            units_val += 1

            return int_to_str(num, num_len, units_val, words)

        return int_to_str(num, len(str(num)), 0, [])
