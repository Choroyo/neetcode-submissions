class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapChar = {}
        mapCount = {}

        for char in s1:
            mapChar[char]= mapChar.get(char, 0) + 1
        
        for r in s2:
            if r in mapChar:
                mapCount[r] = mapCount.get(r, 0) + 1
            else:
                mapCount = {}
            if mapCount == mapChar:
                return True
        return False