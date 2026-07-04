class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        #stop1:[bus1,bus2]
        #stop2:[bus2]
        if source==target:
            return 0

        s_b=defaultdict(list)
        for bus_id, route in enumerate(routes):
            for stop in route:
                s_b[stop].append(bus_id)

        if source not in s_b or target not in s_b:
            return -1

        queue=deque([(source,0)])

        visited_s={source}
        visited_b=set()

        while queue:
            current_stop,bus_taken=queue.popleft()

            for bus_id in s_b[current_stop]:

                if bus_id not in visited_b:
                    visited_b.add(bus_id)

                    for next_stop in routes[bus_id]:
                        if next_stop==target:
                            return bus_taken+1

                        if next_stop not in visited_s:
                            visited_s.add(next_stop)
                            queue.append((next_stop, bus_taken+1))

        return -1















