class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        x = ''
        x_temp = ''
        for i in range(min(l1, l2)):
            if str1[i] != str2[i]:
                break
            x_temp += str1[i]
            if l1 % (i+1) != 0 or l2 % (i+1) != 0:
                continue
            if str1 == x_temp * (l1 // (i+1)) \
                and str2 == x_temp * (l2 // (i+1)):
                x = x_temp
        return x
