class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        self_dividing_nums = []

        while left <= right:
            num = str(left)

            if left < 10:
                self_dividing_nums.append(left)
                left += 1
                continue

            if "0" in num:
                left += 1
                continue

            is_self_dividing = True

            for n in list(num):
                if left % int(n) != 0:
                    is_self_dividing = False

            if is_self_dividing and left not in self_dividing_nums:
                self_dividing_nums.append(left)

            left += 1

        return self_dividing_nums

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(num):
            original_num = num
            while num > 0:
                digit = num % 10
                if digit == 0 or original_num % digit != 0:
                    return False
                num //= 10
            return True

        self_dividing_nums = []
        for num in range(left, right + 1):
            if is_self_dividing(num):
                self_dividing_nums.append(num)

        return self_dividing_nums
