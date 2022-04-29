class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def rec(s, open_rem, close_rem):
            if open_rem == 0:
                return [ s + ")" * close_rem ]
            result = []
            result += rec(s + "(", open_rem-1, close_rem+1)
            if close_rem > 0:
                result += rec(s + ")", open_rem, close_rem-1)
            return result
            
        return rec("", n, 0)
