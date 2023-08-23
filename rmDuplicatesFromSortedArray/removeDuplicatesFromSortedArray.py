# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each 
# unique element appears only once. The relative order of the elements should be kept the same. Then return the 
# number of unique elements in nums. 

# Constraints:
    # 1 <= nums.length <= 3 * 104
    # -100 <= nums[i] <= 100
    # nums is sorted in non-decreasing order.


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        seen_nums = []
        for num in nums:
            if num not in seen_nums:
                seen_nums.append(num)
                

