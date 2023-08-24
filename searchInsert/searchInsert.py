class Solution:
    # def searchInsert(self, nums: list[int], target: int) -> int:
    #     for i in range(len(nums)):
    #         if nums[i] >= target:
    #             return i
    #     return len(nums)


# -------- Binary Search Logic. O(log n)--------
    def searchInsert(self, nums: list[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return left
