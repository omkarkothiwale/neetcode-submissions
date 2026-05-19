class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        ans = 0
        while k>0:
            ans = -heapq.heappop(max_heap)
            k-=1
        return ans