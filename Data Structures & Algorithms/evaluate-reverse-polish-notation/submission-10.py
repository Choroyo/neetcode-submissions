class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        myStack = []
        i = 0

        while i < len(tokens):
            
            if tokens[i].isdigit():
                myStack.append(int(tokens[i]))
            else:
                operand = tokens[i]
                
                num1 = myStack[0]
                myStack.pop(0)
                print(myStack)
                num2 = myStack[0]
                myStack.pop(0)

                if operand == "+":
                    result = num1 + num2
                elif operand == "-":
                    result = num1 - num2
                elif operand == "*":
                    result = num1 * num2
                else:
                    result = (num1 + num2 - 1)  // num2
                    print(result)
                myStack.insert(0,result)
            i += 1
        return myStack[0]