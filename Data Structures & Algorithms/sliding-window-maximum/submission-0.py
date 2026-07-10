class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        output = [max(nums[left:k])]
        

        for right in range(k, len(nums)):
            left += 1
            output.append(max(nums[left:right + 1]))

        return output
