class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(running, selected, index):
            if index == len(nums):
                return
            
            if running == target:
                temp = selected.copy()
                result.append(temp)
                return
            if running > target:
                return

            if nums[index] > target - running:
                return
        
            # repeat num
            selected.append(nums[index])
            backtrack(running + nums[index], selected, index)

            # try next num in arr
            selected.pop()
            backtrack(running, selected, index + 1)

        backtrack(0, [], 0)
        return result