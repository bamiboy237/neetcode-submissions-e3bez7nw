class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for num in num_set:

            if (num-1) in num_set:
                continue

            curr_num = num
            curr_len = 1

            while (curr_num+1) in num_set:
                curr_len += 1
                curr_num += 1
            max_len = max(max_len, curr_len)

        return max_len