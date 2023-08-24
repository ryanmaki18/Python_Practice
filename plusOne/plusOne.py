class Solution:
    # Without a for loop
    def plusOne(self, digits: list[int]) -> list[int]:
        s = ''.join(map(str,digits))
        i = int(s) + 1
        li = list(map(int, str(i)))
        return li

    # # With a for loop
    # def plusOne(self, digits: list[int]) -> list[int]:
    #     for i in range(len(digits)-1, -1, -1):
    #         if digits[i] == 9:
    #             digits[i] = 0
    #         else:
    #             digits[i] += 1
    #             return digits
    #     return [1] + digits