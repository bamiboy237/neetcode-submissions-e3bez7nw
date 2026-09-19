class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s_lower[left].isalnum():
                left += 1
            while left < right and not s_lower[right].isalnum():
                right -= 1
            
            if s_lower[left] != s_lower[right]:
                return False
            
            left += 1
            right -= 1
        return True