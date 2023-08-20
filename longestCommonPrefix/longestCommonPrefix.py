class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""
        sorted_strs = sorted(strs)
        start = sorted_strs[0]   
        end = sorted_strs[-1] 
        for i in range(min(len(start), len(end))):
            if (start[i] != end[i]):
                return result
            result+=start[i]
        return result
