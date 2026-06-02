class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapChar = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        mapCount = mapChar.copy()
        r = len(s1)
        l = 0
        match = 0

        if len(s1) > len(s2):
            return False

        for char in s1:
            mapChar[char] += 1

        for i in range(0, r):
            mapCount[s2[i]] += 1   
            
        for i in range(ord('a'), ord('z') + 1):
            if mapChar[chr(i)] == mapCount[chr(i)]:
                match += 1
        
        if match == 26:
            return True

        while r < len(s2):
            if mapChar[s2[r]] == mapCount[s2[r]]:
                match -= 1

            mapCount[s2[r]] += 1
            if mapChar[s2[r]] == mapCount[s2[r]]:
                match += 1
            
            if mapChar[s2[l]] == mapCount[s2[l]]:
                match -= 1
    
            mapCount[s2[l]] -= 1
            if mapChar[s2[l]] == mapCount[s2[l]]:
                match += 1
            
            l += 1
            r += 1

            if match == 26:
                return True
        return False