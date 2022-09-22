from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        s = Counter(s)
        top,top_count = s.most_common(1)[0]
        del s[top]
        if top_count-1 > s.total():
            return ''
        result = [top for i in range(top_count)]
        index = 0
        for c,count in s.items():
            for i in range(count):
                result[index] += c
                index = (index + 1) % top_count
        return ''.join(result)
