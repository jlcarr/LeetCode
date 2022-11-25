class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # get group ordering via links and topo-sort
        #construct the graph
        group = [item_group if item_group >=0 else -1-item for item,item_group in enumerate(group)]
        groupMembership = dict()
        groupsGraph = dict()
        incommingCounts = dict()
        for item_group in group:
            groupMembership[item_group] = set()
            groupsGraph[item_group] = set()
            incommingCounts[item_group] = 0 
        for item,item_group in enumerate(group):
            groupMembership[item_group].add(item)
        for item in range(n):
            item_group = group[item]
            for other_item in beforeItems[item]:
                if other_item == item:
                    return []
                other_group = group[other_item]
                if other_group == item_group:
                    continue
                if item_group not in groupsGraph[other_group]:
                    incommingCounts[item_group] += 1
                groupsGraph[other_group].add(item_group)
        #print(groupMembership)
        #print(groupsGraph)
        #print(incommingCounts)
        # Kahn's topo-sort
        group_sort = []
        leads = [group for group,incomming in incommingCounts.items() if incomming == 0]
        while leads:
            #print(leads,incommingCounts)
            item_group = leads.pop()
            group_sort.append(item_group)
            # remove from the graph
            for other_group in groupsGraph[item_group]:
                incommingCounts[other_group] -= 1
                if incommingCounts[other_group] == 0:
                    leads.append(other_group)
        #print(group_sort)
        # was a topological sort found?
        if len(group_sort) < len(groupsGraph):
                return []
    
        # within each group do topo-sort
        # append all results together
        result = []
        for item_group in group_sort:
            items = groupMembership[item_group]
            # construct graph
            itemGraph = dict()
            incommingCounts = dict()
            for item in items:
                itemGraph[item] = set()
                incommingCounts[item] = 0
            for item in items:
                for other_item in beforeItems[item]:
                    if other_item in items:
                        itemGraph[other_item].add(item)
                        incommingCounts[item] += 1
            # Kahn's topo-sort
            item_sort = []
            leads = [item for item,incomming in incommingCounts.items() if incomming == 0]
            while leads:
                item = leads.pop()
                item_sort.append(item)
                # remove from the graph
                for other_item in itemGraph[item]:
                    incommingCounts[other_item] -= 1
                    if incommingCounts[other_item] == 0:
                        leads.append(other_item)
            if len(item_sort) < len(itemGraph):
                return []
            result += item_sort
        return result
