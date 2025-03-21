class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        rem = {r:len(l) for r,l in zip(recipes, ingredients)}
        inv = dict()
        for r,l in zip(recipes, ingredients):
            for i in l:
                if i not in inv:
                    inv[i] = set()
                inv[i].add(r)
        result = []
        while supplies:
            i = supplies.pop()
            if i not in inv:
                continue
            for r in inv[i]:
                rem[r] -= 1
                if not rem[r]:
                    result.append(r)
                    supplies.append(r)
        return result
