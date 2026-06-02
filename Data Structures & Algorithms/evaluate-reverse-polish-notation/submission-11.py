class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        myStack = []
        operands = {"+", "-", "/", "*"}
        i = 0

        while i < len(tokens):
            if tokens[i] in operands:
                operand = tokens[i]
                num1 = myStack.pop()
                num2 = myStack.pop()

                if operand == "+":
                    result = num1 + num2
                elif operand == "-":
                    result = num2 - num1
                elif operand == "*":
                    result = num1 * num2
                else:
                    result = int(num2 / num1)
                myStack.append(result)
            else:
                myStack.append(int(tokens[i]))
            i += 1
        return myStack[0]