class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closingBracket = {")" : "(", "]" : "[", "}" : "{"}
        for bracket in s:
            if bracket in closingBracket:
                if stack and stack[-1] == closingBracket[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return not stack
