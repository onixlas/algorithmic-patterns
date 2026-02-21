class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        number = []

        for char in s:
            if char.isdigit():
                number.append(char)
            elif char == "[":
                stack.append("".join(number))
                number = []
            elif char == "]":
                alphas = []
                while stack[-1].isalpha():
                    alphas.append(stack.pop())
                stack.extend(reversed(alphas * int(stack.pop())))
            else:
                stack.append(char)

        return "".join(stack)
