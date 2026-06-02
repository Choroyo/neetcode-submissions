class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0

        if len(s) < 2:
            print(ord(s[0]))
            return 0

        for i in range(len(s) - 1):
            num1 = ord(s[i])
            num2 =  ord(s[i + 1])
            total += abs(num1 - num2)
        
        return total