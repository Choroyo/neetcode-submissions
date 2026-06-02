class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setLetters = set()
        l = 0
        r = 0
        maxLen = 0
         
        while r < len(s) - 1:
            if s[r] in setLetters:
                setLetters.remove(s[l])
                l += 1
            else:
                setLetters.add(s[r])
                maxLen = max(maxLen, len(setLetters))
                print(s[r])
                r += 1
                print(setLetters)

        return maxLen