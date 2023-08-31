import math
from collections import defaultdict

class Solution:
    # # Using sorting method
    # def majorityElement(self, nums: list[int]) -> int:
    #     majority_index = len(nums) // 2
    #     nums.sort()
    #     return nums[majority_index]
    
    # Hash Map
    def majorityElement(self, nums: list[int]) -> int:
        m = defaultdict(int)

        for num in nums:
            m[num] += 1

        n = len(nums) // 2
        for key, value in m.items():
            if value > n:
                return key
        
        return 0

