class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = [folder[0].split('/')]
        for f in folder:
            f = f.split('/')
            #print(result[-1], f)
            startswith = True
            for i,d in enumerate(result[-1]):
                if d != f[i]:
                    startswith = False
                    break
            if not startswith:
                result.append(f)
        return ['/'.join(f) for f in result]
