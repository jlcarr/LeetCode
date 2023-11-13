class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        routes = [set(route) for route in routes] # bus -> stops
        busses = dict() # stop -> busses
        for b,route in enumerate(routes):
            for stop in route:
                if stop not in busses:
                    busses[stop] = set()
                busses[stop].add(b)
        
        q_stops = [source]
        searched_stops = set(q_stops)
        searched_busses = set()

        result = 0
        while q_stops:
            result += 1
            q_busses = []
            for stop in q_stops:
                for bus in list(busses[stop]):
                    if bus not in searched_busses:
                        searched_busses.add(bus)
                        q_busses.append(bus)
                    busses[stop].remove(bus)
            q_stops = []
            for bus in q_busses:
                for stop in list(routes[bus]):
                    if stop == target:
                        return result
                    if stop not in searched_stops:
                        searched_stops.add(stop)
                        q_stops.append(stop)
                    routes[bus].remove(stop)
        return -1
