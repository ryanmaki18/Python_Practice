class Solution:
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     for i in range(len(nums)):
    #         if nums[i] == target:
    #             return i
    #     index = 0
    #     for i in range(len(nums)):
    #         if nums[i] < target:
    #             continue
    #         else:
    #             return i


# -------- Binary Search Logic. O(log n)--------
    def searchInsert(self, nums: List[int], target: int) -> int:
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
