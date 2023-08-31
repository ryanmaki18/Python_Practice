from collections import Counter

class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False

    #     for i in set(s):
    #         # Compare s.count(l) and t.count(l) for every index i from 0 to 26
    #         # If any idx count is different, return false
    #         if s.count(i) != t.count(i):
    #             return False
    #     return True   
    
    # Using built-in counter function
    def isAnagram(self, s: str, t: str) -> bool:
        sCount, tCount = Counter(s), Counter(t)
        return sCount == tCount
    
    # Without using built-in counter function
    def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t):
                return False
        
            counter_s = [0] * 26
            counter_t = [0] * 26
        
            for char in s:
                counter_s[ord(char) - ord('a')] += 1
        
            for char in t:
                counter_t[ord(char) - ord('a')] += 1
            
            return counter_s == counter_t
    
    