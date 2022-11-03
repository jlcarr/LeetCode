from collections import Counter
class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        creators_pop = Counter()
        for c,v in zip(creators,views):
            creators_pop[c] += v
        
        creators_list = dict()
        max_pop = None
        for creator, pop in creators_pop.most_common():
            if not max_pop:
                max_pop = pop
            if pop == max_pop:
                creators_list[creator] = None
            else:
                break
        
        for c,vid,v in zip(creators,ids,views):
            if c not in creators_list:
                continue
            if creators_list[c] is None:
                creators_list[c] = (vid, v)
            else:
                if v > creators_list[c][1] \
                    or (v == creators_list[c][1] and vid < creators_list[c][0]):
                    creators_list[c] = (vid, v)
    
        result = []
        for c,(vid,v) in creators_list.items():
            result.append([c,vid])
        return result
