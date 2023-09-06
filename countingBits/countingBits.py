#Given an integer n, return an array ans of length n + 1 such that for each i...
# ... (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

class Solution:
    # Brute-Force Solution
    def countBits(self, n: int) -> list[int]:
        result = []
        
        for i in range(0, n + 1):
            binary = bin(i)
            one_count = 0
            
            for num in binary[2:]:
                if num == '1':
                    one_count += 1
            result.append(one_count)
        
        return result