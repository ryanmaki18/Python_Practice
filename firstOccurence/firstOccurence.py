
# ------- Three implementations, , a built-in, brute force, and using the KPM algorithm -------
class Solution:
    # ------- Easiest Solution (using built-in find function). Is O(n) -------
    """
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    """


    # ------- Brute Force -------
    """
    def strStr(self, haystack: str, needle: str) -> int:
        N, H = len(needle), len(haystack)

        for i in range(H - N + 1):
            for j in range(N):
                if needle[j] != haystack[i + j]:
                    break
                if j == N - 1:
                    return i
                
        return -1  
    """

    # ------- Using KPM algorithm -------
    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0] * len(needle)

        # Preprocessing
        pre = 0
        for i in range(1, len(needle)):
            while (pre > 0 and
                    needle[i] != needle[pre]):
                pre = lps[pre-1]
            if needle[pre] == needle[i]:
                pre += 1
                lps[i] = pre

        # Main algorithm
        n = 0 #needle index
        for h in range(len(haystack)):
            while (n > 0 and needle[n] != haystack[h]):
                n = lps[n-1]
            if needle[n] == haystack[h]:
                n += 1
            if n == len(needle):
                return h - n + 1

        return -1
        