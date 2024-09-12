from typing import List
from Collections import Counter


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter = Counter(nums)

        for i in counter.keys():
            if counter[i] >= 2:
                indexes = [y for y, x in enumerate(nums) if x == i]

                if len(indexes) == 2 and nums[indexes[0]] == nums[indexes[1]] and abs(indexes[0] - indexes[1]) <= k:
                    return True

                if len(indexes) > 2:
                    for idx in range(0, len(indexes) - 1):
                        a = indexes[idx]
                        b = indexes[idx + 1]

                        if nums[a] == nums[b] and abs(a - b) <= k:
                            return True

        return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}

        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True

            index_map[num] = i

        return False
