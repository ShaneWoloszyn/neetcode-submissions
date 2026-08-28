class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        tMap = {}
        for t in tasks:
            tMap[t] = 1 + tMap.get(t, 0)

        maxHeap = [-cnt for cnt in tMap.values()]
        heapq.heapify(maxHeap)

        q = deque([])

        while maxHeap or q:
            time += 1

            if maxHeap:
                cur = 1 + heapq.heappop(maxHeap)
                if cur != 0:
                    q.append([cur, time + n])
            
            if q:
                if q[0][1] <= time:
                    heapq.heappush(maxHeap, q.popleft()[0])
        
        return time