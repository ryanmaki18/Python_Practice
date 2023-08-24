# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each 
# unique element appears only once. The relative order of the elements should be kept the same. Then return the 
# number of unique elements in nums. 

# Constraints:
    # 1 <= nums.length <= 3 * 104
    # -100 <= nums[i] <= 100
    # nums is sorted in non-decreasing order.


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        k = 1
        for num in range(1, len(nums)):
            if nums[num] != nums[k - 1]:
                nums[k] = nums[num]
                k += 1
        
        return k
