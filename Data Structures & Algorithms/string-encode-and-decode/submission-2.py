class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for char in strs:
            encoded.append(f"{len(char)}#{char}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        i = 0
        str_len = ""
        result = []
        while i < len(s):
            if s[i] != "#":
                str_len += s[i]
                i += 1
            else:
                length = int(str_len)
                str_len = ""
                result.append(s[i + 1: i + 1 +length])
                i += length + 1
        return result

