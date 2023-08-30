class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     result = ''
    #     for char in s:
    #         if char.isalpha():
    #             result += char.lower()
    #         if char.isdigit():
    #             result += char
    #     if result==result[-1::-1]:
    #         return True
    #     else:
    #         return False

    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        left, right = 0, len(cleaned) - 1
        
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        
        return True
