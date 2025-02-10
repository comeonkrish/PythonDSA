class Solution:
    def runningSum(self, nums):
        n = len(nums)

        prefix_sum = [0] * n

        prefix_sum[0] = nums[0]

        for i in range(1,n):
            prefix_sum[i] = nums[i] + prefix_sum[i-1]
            
        print(prefix_sum)

objarray = Solution()
objarray.runningSum([1,1,1,1,1])



        