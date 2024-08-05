class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # counter_arr = Counter(arr)
        # counter_target = Counter(target)
        arr.sort()
        target.sort()

        return arr == target
