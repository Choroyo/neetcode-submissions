class Solution:
    def isPalindrome(self, s: str) -> bool:
        line = ""
        for c in s:
            if isalpha(c):
                line += c
        if line[:-1] == line:
            return True
        return False