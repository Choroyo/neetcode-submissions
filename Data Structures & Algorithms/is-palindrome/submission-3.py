class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            leftL = s[l]
            rightL = s[r]
            if not leftL.isalnum():
                l += 1
                continue
            if not rightL.isalnum():
                r -= 1
                continue
            if leftL != rightL:
                return false
        return True
