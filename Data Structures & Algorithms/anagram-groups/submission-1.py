class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        

        for word in strs:
            words_ascii = [0] * 26
            for char in word:
                words_ascii[ord(char) - ord('a')] += 1
            words[tuple(words_ascii)].append(word)
        
        return list((words.values()))
        



        