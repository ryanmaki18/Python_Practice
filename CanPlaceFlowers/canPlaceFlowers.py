class Solution:
    # def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
    #     count, prev = 0, 0

    #     for cur in flowerbed:
    #         if cur == 1:
    #             if prev == 1: # violation!
    #                 count -= 1
    #             prev = 1
    #         else:
    #             if prev == 1: # can't plant
    #                 prev = 0 
    #             else:
    #                 count += 1
    #                 prev = 1 # the cur plot gets taken
            
    #     return count >= n

            
    # Greedy Approach
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        c=0
        if n==0:
            return True

        if len(flowerbed)==1:
            if flowerbed[0]==0:
                return True
            else:
                return False

        for i in range(len(flowerbed)):
            if i==0:
                if flowerbed[i]==0 and flowerbed[i+1]!=1:
                    flowerbed[i]=1
                    c+=1
            if i==len(flowerbed)-1:
                if flowerbed[i]==0 and flowerbed[i-1]!=1:
                    flowerbed[i]=1
                    c+=1
            if flowerbed[i]==1:
                continue
            else:
                if flowerbed[i-1]!=1 and flowerbed[i+1]!=1:
                    flowerbed[i]=1
                    c+=1
        if c>=n:
            return True
        else:
            return False