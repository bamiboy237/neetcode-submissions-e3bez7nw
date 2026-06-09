class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num, counts in freq.items():
            buckets[counts].append(num)

        res = []
        for bucket in range(len(buckets)-1, 0, -1):
            for n in buckets[bucket]:
                res.append(n)
                if len(res) == k:
                    return res

        
