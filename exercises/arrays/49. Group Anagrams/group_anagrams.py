class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]

        if len(strs) == 1:
            return [strs]

        anagrams = defaultdict(list)

        for str_el in strs:
            anagrams["".join(sorted(str_el))].append(str_el)

        return [ana for ana in anagrams.values()]
