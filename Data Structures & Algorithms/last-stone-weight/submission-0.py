class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            largest = -heapq.heappop(max_heap)
            sec_lar = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -(largest-sec_lar))
        return -max_heap[0]