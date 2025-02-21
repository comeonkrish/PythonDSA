import heapq

class Solution:
    def findKthLargest(self, nums, k):

        heap = nums[:k]
        heapq.heapify(heap)

        print(heap)
    
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)  
                heapq.heappush(heap, num) 
    
        return heap[0]


obj = Solution()
ans = obj.findKthLargest([3,2,1,5,6,4], 2)
print(ans)        
        