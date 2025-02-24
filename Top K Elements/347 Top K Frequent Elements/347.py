import heapq

class Solution:
    def topKFrequent(self, nums, k):
       
        freq_map = {}
    
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
    
        heap = []
    
        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))  
        
            if len(heap) > k:
                heapq.heappop(heap)
    
        top_k_elements = []
    
        while heap:
            _, num = heapq.heappop(heap) 
            top_k_elements.append(num)  
    
        return top_k_elements
    
obj = Solution()
ans = obj.topKFrequent([1,1,1,2,2,3], 2)
print(ans)
