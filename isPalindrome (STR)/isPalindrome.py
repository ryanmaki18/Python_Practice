class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''
        for char in s:
            if char.isalpha():
                result += char.islower()
            if char.isdigit():
                result += char
        if result == reversed(result):
            return True
        return False
