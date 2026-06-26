
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = curr_sum = nums[0]
        
        for right in range(1, len(nums)):
            if curr_sum < 0:
                curr_sum = 0
                
            curr_sum += nums[right]
            
            if max_sum <= curr_sum:
                max_sum = curr_sum
        return max_sum