class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count = 0
        b_count = 0

        for char in s:
            if char == "b":
                b_count += 1
            else:
                a_count += 1

            a_count = min(a_count, b_count)

        return a_count

    def minimumDeletions(self, s: str) -> int:
        deletions_needed = 0
        b_count = 0

        for char in s:
            if char == "b":
                b_count += 1
            else:  # char == 'a'
                if b_count > 0:
                    deletions_needed += 1
                    b_count -= 1

        return deletions_needed
