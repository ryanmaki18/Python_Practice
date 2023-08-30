class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Without converting to String
        if x < 0:
            return False
        input_num = x
        new_num = 0
        while x > 0:
            new_num = (new_num * 10) + (x % 10)
            x = x // 10
        return new_num == input_num

# --------- Converting to string using "::" ---------
    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0:
    #         return False
    #     return str(x) == str(x)[::-1]
    
    
# --------- Converting to string not using "::" ---------
    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0:
    #         return False
        
    #     x_str = str(x)
    #     reversed_str = ''.join(reversed(x_str))
    #     return x_str == reversed_str
    