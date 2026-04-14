class Solution:
    def longestPalindrome(self, s: str) -> str:
        curLongest = ""
        longestLen = 0
        curPos = 0
        n = len(s)
        while curPos < n:
            leftP = curPos
            rightP = curPos
            while leftP >= 0 and rightP < n and s[leftP] == s[rightP]:
                if leftP >= 0 and rightP < n and s[leftP] == s[rightP]  :
                    curLen = len(s[leftP:rightP+1])
                    if curLen> longestLen:
                        longestLen = curLen
                        curLongest = s[leftP:rightP+1]
                leftP -=1
                rightP +=1
            leftP = curPos
            rightP = curPos + 1
            while leftP >= 0 and rightP < n and s[leftP] == s[rightP]:
                if leftP >= 0 and rightP < n and s[leftP] == s[rightP]  :
                    curLen = len(s[leftP:rightP+1])
                    if curLen> longestLen:
                        longestLen = curLen
                        curLongest = s[leftP:rightP+1]
                leftP -=1
                rightP +=1
            curPos +=1

        return curLongest