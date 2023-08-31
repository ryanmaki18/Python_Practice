import math

class Solution:
    # Using sorting method
    def majorityElement(self, nums: list[int]) -> int:
        majority_index = len(nums) // 2
        nums.sort()
        return nums[majority_index]
    
    # FIXME: Work on other implementations
    