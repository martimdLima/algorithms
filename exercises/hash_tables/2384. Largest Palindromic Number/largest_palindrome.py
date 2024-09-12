class Solution:
    def largestPalindromic(self, num: str) -> str:
        nums = list(num)
        nums.sort(reverse=True)

        digits_counter = Counter(nums)
        middle = ""
        palindrome = ""

        if list(digits_counter.keys()) == ["0"]:
            return "0"

        for key, val in digits_counter.items():
            if val > 1:
                if key != 0 or (key == 0 and palindrome != ""):
                    palindrome += f"{key}" * (val // 2)

            digits_counter[key] %= 2

            if digits_counter[key] == 1 and middle == "":
                middle = key
                digits_counter[key] -= 1

        palindrome = palindrome + middle + palindrome[::-1]

        return palindrome.rstrip("0").lstrip("0")

    def largestPalindromic(self, num: str) -> str:
        digits_counter = [0] * 10

        for digit in num:
            digits_counter[int(digit)] += 1

        first_half = []
        middle = ""

        for digit in range(9, -1, -1):
            if digits_counter[digit] > 1:
                first_half.append(str(digit) * (digits_counter[digit] // 2))

            if digits_counter[digit] % 2 == 1 and middle == "":
                middle = str(digit)

        palindrome = "".join(first_half).lstrip("0") + middle + "".join(first_half)[::-1].rstrip("0")

        return "0" if palindrome == "" else palindrome
