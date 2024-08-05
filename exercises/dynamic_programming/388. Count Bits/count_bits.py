class Solution:
    def countBits(self, n: int) -> List[int]:
        return ["{0:b}".format(num).count("1") for num in range(0, n + 1)]

    def countBits(self, n: int) -> List[int]:
        # countBits(x)=countBits(x÷2)+(xmod2)

        # x÷2 effectively shifts the bits of x to the right by one (which is equivalent to  x>>1), which removes the least significant bit.

        # xmod2 checks if the least significant bit is 1 (which is equivalent to x&1).

        bits_count = [0] * (n + 1)

        for i in range(1, n + 1):
            bits_count[i] = bits_count[i >> 1] + (i & 1)

        return bits_count
