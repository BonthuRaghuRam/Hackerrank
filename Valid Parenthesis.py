class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        open = ['(','{','[']
        close = [')','}',']']
        pair = {')':'(','}':'{',']':'['}

        for i in range(len(s)):
            if s[i] in open:
                stack.append(s[i])
            elif s[i] in close:
                if len(stack) == 0 or pair[s[i]] != stack[-1]:
                    return False
                stack.pop()
            else:
                return False
        
        return True if len(stack) == 0 else False
