class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        order = []

        for idx, num in enumerate(nums):
            number = num

            if number == 0:
                order.append((num, mapping[number]))
                continue

            mapped_val = ""

            while number > 0:
                digit = number % 10
                mapped_value = str(mapping[digit])
                mapped_val = mapped_value + mapped_val
                number = number // 10

            order.append((num, int(mapped_val)))

        sorted_tuples = sorted(order, key=lambda x: x[1])

        return [x[0] for x in sorted_tuples]
