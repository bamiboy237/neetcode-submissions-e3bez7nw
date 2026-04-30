class Solution:

    def encode(self, strs: List[str]) -> str:
        padded_strs = ""
        for string in strs:
            padded_strs += str(len(string)) + "#" + string
        return padded_strs

    def decode(self, s: str) -> List[str]:
        res, left_pointer = [], 0

        while left_pointer < len(s):
            right_pointer = left_pointer

            while s[right_pointer] != "#":
                right_pointer += 1
            length = int(s[left_pointer:right_pointer])
            string = s[right_pointer + 1: right_pointer+1+length]
            left_pointer = right_pointer + 1 + length
            res.append(string)
        return res


