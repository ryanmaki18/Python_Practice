class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if not nums:
            return 0
        
        k = 1
        for num in range(1, len(nums)):
            if nums[num] != nums[k - 1]:
                nums[k] = nums[num]
                k += 1
        
        return k
        
        