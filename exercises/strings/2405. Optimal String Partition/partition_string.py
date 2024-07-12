class Solution:
    def partitionString(self, s: str) -> int:
        start = 0
        end = len(s) - 1

        unique_chars = set(s)
        partitions = []
        current_partition = []

        while start <= end:
            char = s[start]
            if char in unique_chars:
                if len(current_partition) > 0:
                    partitions.append("".join(current_partition))
                current_partition = [char]
                unique_chars = {char}
            else:
                current_partition.append(char)
                unique_chars.add(char)
            start += 1

        partitions.append("".join(current_partition))

        return len(partitions)
