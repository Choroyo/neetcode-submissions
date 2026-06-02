class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = 0

        while len(tokens) > 1:
            num1 = int(tokens[0])
            tokens.pop(0)

            num2 = int(tokens[0])
            tokens.pop(0)
            
            operand = tokens[0]
            tokens.pop(0)

            if operand == "+":
                result = num1 + num2
            elif operand == "-":
                result = num1 - num2
            elif operand == "*":
                result = num1 * num2
            else:
                result = num1 / num2
            
            tokens.insert(0, result)
        
        return tokens[0]