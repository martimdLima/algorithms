class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter = Counter({"5": 0, "10": 0, "20": 0})

        for idx, bill in enumerate(bills):
            exchange = bill - 5

            if exchange == 15:
                if counter["10"] < 0:
                    return False

                if counter["10"] > 0:
                    counter["10"] -= 1
                    counter["5"] -= 1
                elif counter["10"] == 0:
                    counter["5"] -= 3

            elif exchange == 5:
                counter["5"] -= 1
                counter["10"] += 1
            else:
                counter["5"] += 1

            if counter["5"] < 0 or counter["10"] < 0 or counter["20"] < 0:
                return False

            print(idx, bill, counter)

        return True

    def lemonadeChange(self, bills: List[int]) -> bool:
        five_count = 0
        ten_count = 0

        for bill in bills:
            if bill == 5:
                five_count += 1
                continue

            if bill == 10:
                if five_count == 0:
                    return False
                five_count -= 1
                ten_count += 1
                continue

            if bill == 20:
                if ten_count > 0 and five_count > 0:
                    ten_count -= 1
                    five_count -= 1
                    continue

                if five_count >= 3:
                    five_count -= 3
                    continue

                if not (ten_count > 0 and five_count > 0) or five_count <= 3:
                    return False

        return True
