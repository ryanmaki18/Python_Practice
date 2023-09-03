class Solution:
    # Brute Force
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found
    
    # # Using Hash Map
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    #     hash_map = {}
    #     for i, num in enumerate(nums):
    #         complement = target - num
    #         if complement in hash_map:
    #             return [hash_map[complement], i]
    #         else:
    #             hash_map[num] = i
    #     return []
        
    
if __name__ == "__main__":
    solution = Solution()

    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    print(result1)  # should print [0, 1]

    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    print(result2)  # should print [1, 2]

    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    print(result3)  # should print [0, 1]

    nums4 = [2, 7, 11, 15]
    target4 = 8
    result4 = solution.twoSum(nums4, target4)
    if len(result4) == 0:
        print("Could not find target sum in the given array")
    else:
        print(result4)  # should print []