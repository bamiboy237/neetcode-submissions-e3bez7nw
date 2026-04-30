from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = defaultdict(int)
        freq_list = [[] for _ in range(len(nums) + 1)]

        for i in nums:
            freq_count[i] += 1

        for num, count in freq_count.items():
            freq_list[count].append(num)

        res = []
        for i in range(len(freq_list)-1, 0, -1):
            for n in freq_list[i]:
                res.append(n)
                if len(res) == k:
                    return res


        