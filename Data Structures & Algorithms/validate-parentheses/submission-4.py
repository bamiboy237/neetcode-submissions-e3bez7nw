class Solution:
    def isValid(self, s: str) -> bool:
        pairs = ["()", "[]", "{}"]

        for _ in range(len(s)):
            for pair in pairs:
                s = s.replace(pair, "")

        return s == ""