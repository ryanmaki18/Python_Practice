class Solution:
    # Brute Force
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     n = len(nums)
    #     for i in range(n - 1):
    #         for j in range(i + 1, n):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]
    #     return []  # No solution found
    
    # Using Hash Map
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]
            else:
                hash_map[num] = i
        return []
