class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if seen.get(complement, None) != None:
                return [seen[complement], i]
            else:
                seen[num] = i