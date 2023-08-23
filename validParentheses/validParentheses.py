class Solution:
    def isValid(self, s: str) -> bool:
        valid_chars = {'(', ')', '{', '}', '[', ']'}
        open_to_close = {')': '(', '}': '{', ']': '['}
        stack = []

        if 1 <= len(s) <= 10**4:
            for char in s:
                if char not in valid_chars:
                    return False
                if char in open_to_close.values():
                    stack.append(char)
                elif char in open_to_close.keys():
                    if not stack or stack.pop() != open_to_close[char]:
                        return False
            return len(stack) == 0
        else: 
            return False