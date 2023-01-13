class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        G = dict()
        for i,p in enumerate(parent):
            if i not in G:
                G[i] = set()
            if p not in G:
                G[p] = set()
            G[p].add(i)

        def rec(curr):
            # return the not-ending and ending
            unconstrained = 0
            top1, top2 = 0, 0
            for c in G[curr]:
                sub_unconstrained, sub_ending = rec(c)
                # possible solution from below
                unconstrained = max(unconstrained, sub_unconstrained)
                # look for longest path up
                if s[c] != s[curr]:
                    if top1 is None or sub_ending > top1:
                        if top2 is None or top1 > top2:
                            top2 = top1
                        top1 = sub_ending
                    elif top2 is None or sub_ending > top2:
                        top2 = sub_ending
            # compute possible solution including
            ending = 1
            sub_unconstrained = 1
            if top1 is not None:
                sub_unconstrained += top1
                ending = top1+1
            if top2 is not None:
                sub_unconstrained += top2
            unconstrained = max(unconstrained, sub_unconstrained)
            #print(curr, '->', unconstrained, ending)
            return unconstrained, ending

        return rec(0)[0]

