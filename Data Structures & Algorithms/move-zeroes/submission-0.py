class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        placement = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[placement], nums[i] = nums[i], nums[placement]

                placement += 1
                
        