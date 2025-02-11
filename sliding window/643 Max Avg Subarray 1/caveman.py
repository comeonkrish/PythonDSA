class Solution:
    def findMaxAverage(self, nums, k: int) -> float:

        current_sum = sum(nums[:k])
        max_avg = current_sum / k
        
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_avg = max(max_avg, current_sum / k)
        
        return max_avg

obj = Solution()
ans = obj.findMaxAverage([1,12,-5,-6,50,3], 4)
print(ans)