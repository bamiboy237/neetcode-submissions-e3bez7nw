class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_idx = abbr_idx = 0

        while abbr_idx < len(abbr):
            if abbr[abbr_idx].isdigit():
                if abbr[abbr_idx] == "0":
                    return False

                j = abbr_idx
                while j < len(abbr) and abbr[j].isdigit():
                    j += 1

                num = int(abbr[abbr_idx:j])
                abbr_idx = j
                word_idx += num

            else:
                if word_idx >= len(word) or word[word_idx] != abbr[abbr_idx]:
                    return False

                word_idx += 1
                abbr_idx += 1

        return word_idx == len(word)