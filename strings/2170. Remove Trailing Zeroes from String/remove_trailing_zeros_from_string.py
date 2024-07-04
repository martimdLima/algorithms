class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        if "0" not in num:
            return num

        ridx = None
        for i in range(len(num) - 1, -1, -1):
            if num[i] != "0":
                break
            ridx = i

        return str(num[:ridx])
