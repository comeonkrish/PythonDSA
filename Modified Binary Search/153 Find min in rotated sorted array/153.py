class Solution:
    def findMin(self, nums):

        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left<right:

            mid = (left + right)//2

            if nums[mid] > nums[right]: # min element in the right half
                left = mid + 1
            else: # min element in the left half
                right = mid 

        return nums[left]

obj = Solution()
ans = obj.findMin([3,4,5,1,2])
print(ans)
