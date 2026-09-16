class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for j in range(len(nums)):
            complement = target - nums[j]
            if complement in hashmap and hashmap[complement] != j:
                return [j, hashmap[complement]]