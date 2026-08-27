class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False
        if s[0] in {')', '}', ']'}:
            return False
        for i in range(len(s)):
            if s[i] in {'(', '{', '['}:
                stack.append(s[i])
            else:
                if stack:
                    if stack[-1]  == '(' and s[i] == ')':
                        stack.pop()
                    elif stack[-1]  == '[' and s[i] == ']':
                        stack.pop()
                    elif stack[-1]  == '{' and s[i] == '}':
                        stack.pop()
                    else:
                        return False
        if stack:
            return False
        return True
