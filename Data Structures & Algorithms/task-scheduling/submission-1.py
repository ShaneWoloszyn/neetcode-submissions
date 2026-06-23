class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        minHeap = [-cnt for cnt in count.values()]
        heapq.heapify(minHeap)

        q = deque([])
        time = 0

        while q or minHeap:
            time += 1
            print(minHeap)
            print(q)
            if minHeap:
                val = 1 + heapq.heappop(minHeap)
                if val != 0:
                    q.append([val, time + n])
            
            if q and q[0][1] == time:
                val, hold = q.popleft()
                heapq.heappush(minHeap, val)

        return time