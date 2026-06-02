class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapChar = {}
        mapCount = {}
        r = len(s1)
        l = 0
        for char in s1:
            mapChar[char]= mapChar.get(char, 0) + 1
        
        while r <= len(s2):
            print(r, len(s2))
            for c in range(l, r):
                mapCount[s2[c]] = mapCount.get(s2[c], 0) + 1
            if mapCount == mapChar:
                return True
            print(mapCount, mapChar)
            mapCount = {}
            l += 1
            r += 1
            print(r, len(s2))
            
        return False