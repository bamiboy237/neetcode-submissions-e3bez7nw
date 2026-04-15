class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        freq = sorted(list(count.values()))[-k:]
        return [key for key, value in count.items() if value in freq ]


