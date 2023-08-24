class Solution:
    # ------ One line implmentation ------
    def addBinary(self, a: str, b: str) -> str:
        # Converts to ints to do computation, then slices off "Ob"
        return bin(int(a, 2) + int(b, 2))[2:]

    # # ------ More readable answer uses a loop  ------
    # # Iterates through the binary strings right to left, like manual binary
    # # addition is done
    # def addBinary(self, a: str, b: str) -> str:
    #     s = []
    #     carry = 0
    #     i = len(a) - 1
    #     j = len(b) - 1

    #     while i >= 0 or j >= 0 or carry:
    #         if i >= 0:
    #             carry += int(a[i])
    #             i -= 1
    #         if j >= 0:
    #             carry += int(b[j])
    #             j -= 1
    #         s.append(str(carry % 2))
    #         carry //= 2

    #     return ''.join(reversed(s))
