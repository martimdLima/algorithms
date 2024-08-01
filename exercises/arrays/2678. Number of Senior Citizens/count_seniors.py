class Solution:
    def countSeniors(self, details: List[str]) -> int:
        num_pass = 0

        for detail in details:
            age = detail[11:13]
            if int(age) > 60:
                num_pass += 1

        return num_pass

    def countSeniors(self, details: List[str]) -> int:
        return sum(1 for detail in details if int(detail[11:13]) > 60)
