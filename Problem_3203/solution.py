class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        #print('start')
        # find leaves, retract and get min depths, join by 1
        G = dict()
        for e in edges1:
            if e[0] not in G:
                G[e[0]] = set()
            G[e[0]].add(e[1])
            if e[1] not in G:
                G[e[1]] = set()
            G[e[1]].add(e[0])
        if not G:
            G[0] = set()
            
        # check own diameter
        dists = {k:-1 for k in G.keys()}
        dists[0] = 0
        stack = [0]
        while stack:
            curr = stack.pop()
            for child in G[curr]:
                if dists[child] == -1:
                    dists[child] = dists[curr] + 1
                    stack.append(child)
        maxi = 0
        maxd = 0
        for i,d in dists.items():
            if d > maxd:
                maxd = d
                maxi = i
        dists = {k:-1 for k in G.keys()}
        dists[maxi] = 0
        stack = [maxi]
        while stack:
            curr = stack.pop()
            for child in G[curr]:
                if dists[child] == -1:
                    dists[child] = dists[curr] + 1
                    stack.append(child)
        diameter1 = max(dists.values())
        #print('diameter1', diameter1)
        
        # search
        depth1 = 0
        leaves = set([k for k in G if len(G[k]) == 1])
        while leaves:
            #print('leaves1', leaves)
            depth1 += 1
            if len(G) <= 2:
                break
            new_leaves = set()
            for leaf in leaves:
                #print('leaf', leaf)
                parent = G[leaf].pop()
                del G[leaf]
                G[parent].remove(leaf)
                if len(G[parent]) == 0:
                    new_leaves = set()
                    break
                if len(G[parent]) == 1:
                    new_leaves.add(parent)
            leaves = new_leaves
        #print('depth1', depth1)

        
        # find leaves, retract and get min depths, join by 1
        G = dict()
        for e in edges2:
            if e[0] not in G:
                G[e[0]] = set()
            G[e[0]].add(e[1])
            if e[1] not in G:
                G[e[1]] = set()
            G[e[1]].add(e[0])
        if not G:
            G[0] = set()
        
        # check own diameter
        dists = {k:-1 for k in G.keys()}
        dists[0] = 0
        stack = [0]
        while stack:
            curr = stack.pop()
            for child in G[curr]:
                if dists[child] == -1:
                    dists[child] = dists[curr] + 1
                    stack.append(child)
        maxi = 0
        maxd = 0
        for i,d in dists.items():
            if d > maxd:
                maxd = d
                maxi = i
        dists = {k:-1 for k in G.keys()}
        dists[maxi] = 0
        stack = [maxi]
        while stack:
            curr = stack.pop()
            for child in G[curr]:
                if dists[child] == -1:
                    dists[child] = dists[curr] + 1
                    stack.append(child)
        diameter2 = max(dists.values())
        #print('diameter2', diameter2)
        
        # search
        depth2 = 0
        leaves = set([k for k in G if len(G[k]) == 1])
        while leaves:
            #print('leaves2', leaves)
            depth2 += 1
            if len(G) <= 2:
                break
            new_leaves = set()
            for leaf in leaves:
                #print('leaf', leaf)
                parent = G[leaf].pop()
                del G[leaf]
                G[parent].remove(leaf)
                if len(G[parent]) == 0:
                    new_leaves = set()
                    break
                if len(G[parent]) == 1:
                    new_leaves.add(parent)
            leaves = new_leaves
        #print('depth2', depth2)
        
        return max(depth1 + depth2 + 1, diameter1, diameter2)
            
