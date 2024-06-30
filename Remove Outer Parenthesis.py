class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cnt=0
        result=""
        for i in s:
            if i=='(':
                cnt+=1
                if cnt>1:
                    result+=i
            elif i==')':
                cnt-=1
                if cnt>0:
                    result+=i
        return result
        
