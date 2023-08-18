from collections import Counter
from itertools import combinations
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads:
            return 0
        cityRanks = Counter()
        connections = set()
        for city1,city2 in roads:
            cityRanks[city1] += 1
            cityRanks[city2] += 1
            connections.add((min(city1,city2), max(city1,city2)))
        cityRanks = cityRanks.most_common()
        top_deg = cityRanks[0][1]
        # if more than 1 top degree, then find best pair
        if top_deg == cityRanks[1][1]:
            candidates = []
            for city,deg in cityRanks:
                if deg != top_deg:
                    break
                candidates.append(city)
            candidates.sort()
            for citypair in combinations(candidates, 2):
                #print("p", citypair)
                if citypair not in connections:
                    print(citypair)
                    return 2 * top_deg
            #print(cityRanks[0][0], cityRanks[1][0])
            return 2 * top_deg - 1
        # if only 1 top degree, then find best of second
        top_city = cityRanks[0][0]
        next_deg = cityRanks[1][1]
        for city,deg in cityRanks:
            if deg == top_deg:
                continue
            if deg < next_deg:
                break
            if (min(top_city,city), max(top_city,city)) not in connections:
                #print(top_city,city)
                return top_deg + next_deg
        #print(top_city,cityRanks[1][0])
        return top_deg + next_deg - 1
