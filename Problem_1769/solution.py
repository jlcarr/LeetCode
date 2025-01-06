class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        t = boxes.count('1')
        prevs = 0
        prevs_dist = 0
        posts = t
        posts_dist = sum(i for i,v in enumerate(boxes) if v == '1')
        result = []
        for v in boxes:
            if v == '1':
                posts -= 1
                prevs += 1
            result.append(prevs_dist + posts_dist)
            posts_dist -= posts
            prevs_dist += prevs
        return result
