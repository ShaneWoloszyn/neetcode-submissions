class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        arr = [-cnt for cnt in count.values()]
        heapq.heapify(arr)
        
        q = deque([])

        time = 0

        while arr or q:
            time += 1
            if not arr:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(arr)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(arr, q.popleft()[0])
            

        return time