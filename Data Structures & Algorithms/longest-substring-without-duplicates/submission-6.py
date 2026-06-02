class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setLetters = set()
        l = 0
        r = 0
        maxLen = 0

        while r < len(s):
            if s[r] in setLetters:
                setLetters.remove(s[l])
                l += 1
                print("here")
            else:
                setLetters.add(s[r])
                maxLen = max(maxLen, len(setLetters))
                print(s[r].isspace)
                r += 1
                print(setLetters)

        return maxLen