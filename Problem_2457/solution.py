def digsum(x):
    result = 0
    while x:
        result += x % 10
        x //= 10
    return result

class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        x = 0
        pos_acc = 1
        while True:
            d = ((n+x) // pos_acc) % 10
            #print(pos_acc, d)
            if d > 0:
                c = 10-d
                for i in range(c+1):
                    #print(x, i, pos_acc, n + x + i * pos_acc, digsum(n + x + i * pos_acc))
                    if digsum(n + x + i * pos_acc) <= target:
                        return x + i * pos_acc
                x += c * pos_acc
            pos_acc *= 10
                
