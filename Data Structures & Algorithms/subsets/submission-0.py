class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(selected, index):
            if (index == len(nums)):
                temp = selected.copy()
                result.append(temp)
                return

            # include
            selected.append(nums[index])
            backtrack(selected, index + 1)
            selected.pop()
        
            # exclude
            backtrack(selected, index + 1)
        backtrack([], 0)
        return result