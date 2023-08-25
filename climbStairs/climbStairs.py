class Solution:
    # ------------ Implmentations using Dynamic Programming ------------
    # ------ Implementation using Memotization ------
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.memo_helper(n, memo)
    
    def memo_helper(self, n: int, memo: dict[int, int]) -> int:
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = self.memo_helper(n-1, memo) + self.memo_helper(n-2, memo)
        return memo[n]
    
    # # ------ Implementation using Tabulation ------
    # def climbStairs(self, n: int) -> int:
    #     if n == 0 or n == 1:
    #         return 1

    #     dp = [0] * (n+1)
    #     dp[0] = dp[1] = 1
        
    #     for i in range(2, n+1):
    #         dp[i] = dp[i-1] + dp[i-2]
    #     return dp[n]

