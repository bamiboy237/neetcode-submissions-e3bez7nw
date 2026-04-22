from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        groupedAnagrams = []

        for string in strs:
            anagrams["".join(sorted(string))].append(string)
        for key, value in anagrams.items():
            groupedAnagrams.append(value)
        return groupedAnagrams
            