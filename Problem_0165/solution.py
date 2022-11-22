class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int, version1.split('.')))
        version2 = list(map(int, version2.split('.')))
        #print(version1, version2)
        while len(version1) < len(version2):
            version1.append(0)
        while len(version2) < len(version1):
            version2.append(0)
        #print(version1, version2)
        #print()
        if version1 < version2:
            return -1
        elif version1 > version2:
            return 1
        return 0
