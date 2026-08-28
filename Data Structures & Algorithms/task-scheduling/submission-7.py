class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tMap = Counter(tasks)
        maxHeap = [-cnt for cnt in tMap.values()]
        heapq.heapify(maxHeap)

        time = 0

        q = deque([])

        while maxHeap or q:
            time += 1

            if maxHeap:
                cur = heapq.heappop(maxHeap) + 1
                if cur != 0:
                    q.append([cur, time + n])
            
            if q:
                if q[0][1] <= time:
                    heapq.heappush(maxHeap, q.popleft()[0])
        
        return time