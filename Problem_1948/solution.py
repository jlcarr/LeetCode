class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = {'PARENT': dict(), 'NAME': '/'}
        for path in paths:
            curr = root
            for f in path:
                if f not in curr:
                    curr[f] = {'PARENT': curr, 'NAME': f}
                    #curr[f] = dict()
                curr = curr[f]
        #print(root)
        hashes = dict()
        def dfs(curr):
            if len(curr) == 2:
                return 0
            h = 0
            for k,child in list(curr.items()):
                if k != 'PARENT' and k != 'NAME':
                    h += hash(child['NAME']) * (1+dfs(child))
            h = hash(str(h))
            if h in hashes:
                #print(curr['NAME'], hashes[h]['NAME'])
                curr['PARENT'].pop(curr['NAME'], None)
                hashes[h]['PARENT'].pop(hashes[h]['NAME'], None)
            else:
                hashes[h] = curr
            return h
        dfs(root)
        #print({k:v['NAME'] for k,v in hashes.items()})

        def dfs2(curr):
            result = []
            for k,child in curr.items():
                if k != 'PARENT' and k != 'NAME':
                    result += dfs2(child)
            if curr['NAME'] == '/':
                return result
            return [[curr['NAME']]] + [[curr['NAME']] + path for path in result]
        return dfs2(root)


