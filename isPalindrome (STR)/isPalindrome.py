class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 0:
            return False
        
        reversed_str = ''.join(reversed(s))
        return s == reversed_str
    