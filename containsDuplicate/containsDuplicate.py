class Solution:
    # # Implementation using the Set() built-in. Is O(n)
    # def containsDuplicate(self, nums: list[int]) -> bool:
    #     num_set = set()
    #     for num in nums:
    #         if num in num_set:
    #             return True
    #         else:
    #             num_set.add(num)
    #     return False

    # Better way of implementation if using a set. Much cleaner and easier
    def containsDuplicate(self, nums: list[int]) -> bool:
       if len(nums) == len(set(nums)):
           return False
       return True

    # #Implementation using Hash Map. Is O(n).
    # def containsDuplicate(self, nums: list[int]) -> bool:
    #     num_set = {}
    #     for num in nums:
    #         if num in num_set and num_set[num] >= 1:
    #             return True
    #         else:
    #             num_set[num] = num_set.get(num, 0) + 1
    #     return False
    
    # # Using Sorting Method
    # def containsDuplicate(self, nums: list[int]) -> bool:
    #     nums.sort()
    #     n = len(nums)
    #     for i in range(1, n):
    #         if nums[i] == nums[i - 1]:
    #             return True
    #     return False        
    