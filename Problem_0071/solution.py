import re
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path + '/'

        # removed current directories
        l = len(path)
        while True:
            path = re.sub(r'/\./', '/', path)
            if len(path) == l:
                break
            l = len(path)
        # remove double-slashes
        path = re.sub(r'/+', '/', path)

        
        # remove up-directories
        l = len(path)
        while True:
            path = re.sub(r'/[\w_\.]+/\.\./', '/', path, 1)
            if len(path) == l:
                break
            l = len(path)
        path = path.replace('/../', '/')
        
        # remove final slash
        if len(path) > 1:
            path = path[:-1]
        return path
