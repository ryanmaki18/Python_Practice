#Given an integer n, return an array ans of length n + 1 such that for each i...
# ... (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

class Solution:
    def countBits(self, n: int) -> list[int]:
        result = []
        for i in range(0, n + 1):
            binary = bin(i)
            print(binary[2:])

            if binary[2:].contains(1):

        return none