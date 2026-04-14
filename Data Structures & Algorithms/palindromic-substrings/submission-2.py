class Solution:
    def countSubstrings(self, s: str) -> int:
        c = 0
        curPos = 0
        n = len(s)
        while curPos < n:
            leftP = curPos
            rightP = curPos
            while leftP >= 0 and rightP < n and s[leftP] == s[rightP]:
                c+=1
                leftP -=1
                rightP +=1
            leftP = curPos
            rightP = curPos + 1
            while leftP >= 0 and rightP < n and s[leftP] == s[rightP]:
                c+=1
                leftP -=1
                rightP +=1
            curPos +=1

        return c