class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if not nums:
            return 0
        
        k = 0
        for num in range(len(nums)):
            if nums[num] != val:
                nums[k] = nums[num]
                k += 1
        
        return k
        