from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = defaultdict(int)
        k_freq = []
        for i in nums:
            freq_count[i] += 1

        for key, value in freq_count.items():
            k_freq.append((key, value))

        k_freq.sort(key=lambda x: x[1], reverse=True)
        res = [num for num, freq in k_freq]
        return res[:k]