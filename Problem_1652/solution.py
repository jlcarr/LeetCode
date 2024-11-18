class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        l = len(code)
        if k == 0:
            return [0] * l
        elif k > 0:
            acc = sum([code[i % l] for i in range(k)])
            result = []
            for i,v in enumerate(code):
                acc += code[(i+k) % l] - v
                result.append(acc)
        else:
            acc = sum([code[(-i-1) % l] for i in range(-k)])
            result = []
            for i,v in enumerate(code):
                result.append(acc)
                acc += v - code[(i+k) % l]
        return result
