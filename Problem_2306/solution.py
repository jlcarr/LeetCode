class Solution:
    def distinctNames(self, ideas: List[str]) -> int:        
        pref2suf = dict()
        for idea in ideas:
            # pref2suf
            if idea[0] not in pref2suf:
                pref2suf[idea[0]] = set()
            pref2suf[idea[0]].add(idea[1:])

        result = 0
        for c1,suff1 in pref2suf.items():
            for c2,suff2 in pref2suf.items():
                # We aren't interested in any words belong to both categories
                # They are invalid swaps
                intersection = len(suff1 & suff2)
                # Removed our uninterested words, and we can swap all pairs
                result += (len(suff1) - intersection) * (len(suff2) - intersection)

        return result

