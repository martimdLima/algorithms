class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        while n >= 1:
            if n % 3 == 0 and n % 5 == 0:
                result.append("FizzBuzz")
            elif n % 3 == 0:
                result.append("Fizz")
            elif n % 5 == 0:
                result.append("Buzz")
            else:
                result.append(f"{n}")
            n -= 1

        return list(reversed(result))
