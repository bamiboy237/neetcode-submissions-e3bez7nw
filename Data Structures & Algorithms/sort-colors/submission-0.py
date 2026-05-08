class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, mid, right = 0, 0, len(nums) - 1

        while mid <= right:
            if nums[mid] == 0:
                # we interchange the element at index mid and index left
                nums[mid], nums[left] = nums[left], nums[mid]
                left += 1
                mid += 1
            elif nums[mid] == 2:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1
                # we do not increase mid, because we do not know if the element that was formerly at index
                # 2 is a zero, one or two
            else:
                mid += 1
                

