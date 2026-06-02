class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        valid = []

        def backtracking(open, close):
            if close == open == n:
                valid.append("".join(stack))
                return
            if open < n:
                stack.append("(")
                backtracking(open + 1, close)
                stack.pop

            if close < open:
                stack.append(")")
                backtrack(open, close + 1)
                stack.pop

        backtracking(0,0)

        return valid