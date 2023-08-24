class Solution:
    # ------ Easiest Solution ------
    # def lengthOfLastWord(self, s: str) -> int:
    #     res=s.split()
    #     return len(res[-1])

    ## ------ Can be done in one line as well. Not as readable. ------
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
