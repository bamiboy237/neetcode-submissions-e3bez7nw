class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(running, selected, index):
            if index == len(nums):
                return
            temp = selected.copy()
            if running == target:
                result.append(temp)
                return
            if running > target:
                return
        
            # repeat num
            selected.append(nums[index])
            backtrack(running + nums[index], selected, index)

            # try next num in arr
            selected.pop()
            backtrack(running, selected, index + 1)

        backtrack(0, [], 0)
        return result