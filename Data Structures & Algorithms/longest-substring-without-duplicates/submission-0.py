class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        state = {}
        start = 0
        max_len = 0

        for end in range(len(s)):
            if s[end] in state and state[s[end]] >= start:
                start = state[s[end]] + 1
            
            state[s[end]] = end

            max_len = max(max_len, ((end - start) + 1))

        return max_len
        