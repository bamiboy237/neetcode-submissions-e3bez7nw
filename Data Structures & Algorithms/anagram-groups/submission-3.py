from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        groupedAnagrams = []
        

        for string in strs:
            string_key = [0] * 26
            for i in range(len(string)):
                string_char = ord(string[i]) - ord('a')
                string_key[string_char] += 1
            anagrams[tuple(string_key)].append(string)
        for key, value in anagrams.items():
            groupedAnagrams.append(value)
        return groupedAnagrams
            