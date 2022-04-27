class Solution:
    dig_map = { 
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }
    def letterCombinations(self, digits: str) -> List[str]:
        result = [""]
        for d in digits:
            new_result = []
            for c in self.dig_map[d]:
                for ans in result:
                    new_result.append(ans+c)
            result = new_result
        if len(result) == 1:
            return []
        return result
