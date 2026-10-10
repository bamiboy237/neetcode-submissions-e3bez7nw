class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        arr = [word for word in s if word.isalnum()]
        l = 0
        r = len(arr) - 1

        while l < r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        return True        