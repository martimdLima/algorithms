class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        frequency = Counter(arr)

        distinct_count = 0
        for s in arr:
            if frequency[s] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return s

        return ""

    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct = []
        for s in arr:
            if arr.count(s) == 1:
                distinct.append(s)

        if distinct == arr:
            return distinct[k - 1]

        if k <= len(distinct):
            return distinct[k - 1]

        return ""
