class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list)
        for s in strs:
            cArray = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                cArray[index] +=1
            strMap[tuple(cArray)].append(s)
        return list(strMap.values())