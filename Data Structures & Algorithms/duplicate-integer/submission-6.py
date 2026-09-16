from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = defaultdict(int)
        for num in nums:
            if hashmap[num] >= 1:
                return True
            hashmap[num] += 1
        return False