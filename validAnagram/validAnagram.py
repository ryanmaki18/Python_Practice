class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for idx in set(s):
            # Compare s.count(l) and t.count(l) for every index i from 0 to 26...
            # If any idx count is different, return false...
            if s.count(idx) != t.count(idx):
                return False
        return True   