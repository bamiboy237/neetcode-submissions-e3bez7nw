from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result = []
        counts = Counter(s)

        for char in order:
            while counts[char] > 0:
                result.append(char)
                counts[char] -= 1
                if counts[char] == 0:
                    del counts[char]

        for char, count in counts.items():
            for i in range(count):
                result.append(char)
        
        return "".join(result)

        