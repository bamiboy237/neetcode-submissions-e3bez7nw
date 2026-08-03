from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = Counter(nums)
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in num_freq.items():
            freq_buckets[freq].append(num)
        return [num for bucket in freq_buckets for num in bucket][-k:]
