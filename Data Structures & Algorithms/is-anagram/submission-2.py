class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = sorted(s)
        t_list = sorted(t)
        if len(s_list) != len(t_list):
            return False
        for i in range(len(s_list)):
            if s_list[i] != t_list[i]:
                return False
        return True
        