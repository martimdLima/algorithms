class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            index = 1
            while index <= len(digits) and digits[-index] == 9:
                digits[-index] = 0
                if index + 1 < len(digits) and digits[-index - 1] != 9:
                    digits[-index - 1] += 1
                    return digits
                elif index + 1 == len(digits) and digits[-index - 1] <= 8:
                    digits[-index - 1] += 1
                    return digits
                elif index - 1 == len(digits) - 1 and digits[index - 1] != 9:
                    digits = [1] + digits
                    return digits
                index += 1

        digits[-1] += 1
        return digits

    def plusOne(digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        return [1] + digits
