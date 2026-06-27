class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        state = defaultdict(int)
        length = 0

        if not s:
            return length

        for end in range(len(s)):
            state[s[end]] += 1

            while(state[s[end]]) > 1:
                state[s[start]] -= 1
                if state[s[start]] == 0:
                    del state[s[start]]
                start += 1

            length = max(length, end - start + 1)

        return length