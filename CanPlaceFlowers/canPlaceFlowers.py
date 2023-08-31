class Solution:
    # Non-Greedy Approach
    # def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        





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